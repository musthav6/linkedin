import logging
import pickle

import requests
from requests_oauthlib import OAuth2Session
import os
class LinkedInToken:
    def __init__(self, client_id, client_secret, redirect_uri, access_token_file):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'
        self.token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
        self.access_token_file = access_token_file


    def token_file_exists(self):
        return os.path.exists(self.access_token_file) and os.path.getsize(self.access_token_file) > 0

    # def get_token_from_file(self):
    #     try:
    #         with open(self.access_token_file, "r") as file:
    #             token = file.read().strip()
    #             return token
    #     except FileNotFoundError as e:
    #         logging.error(f"File error when token retrieving: {e}")

    def load_token(self):
        try:
            with open(self.access_token_file, "rb") as file:
                token = pickle.load(file)
            return token
        except Exception as e:
            print(f"Error loading token: {e}")
            return None

    def token_validated(self):
        token = ''
        if self.token_file_exists():
            token = self.load_token()
        else:
            return False
        session =  OAuth2Session(client_id=self.client_id,redirect_uri=self.redirect_uri,token=token)
        url = "https://api.linkedin.com/v2/userinfo"

        try:
            response = session.get(url)
            print(response)
            if response.status_code == 200:
                logging.info("Access token is valid.")
                return True
            else:
                logging.warning(f"Access token is invalid or expired: {response.status_code}, {response.json()}")
                return False
        except Exception as e:
            logging.error(f"Error checking token validity: {e}")
            print("Error checking token validity.")
            return False

    def get_session(self):

        session =  OAuth2Session(self.client_id, redirect_uri=self.redirect_uri)

        try:
            authorization_url, state = session.authorization_url(self.authorization_base_url)
            logging.info("Authorization URL generated successfully.")
            print('Go to authorization:', authorization_url + '&scope=profile,email,openid')
        except Exception as e:
            logging.error(f"Error generating authorization URL: {e}")
            return None

        try:
            authorization_response = input('Insert URL after redirecting: ')
            session.fetch_token(self.token_url, client_secret=self.client_secret,
                                 authorization_response=authorization_response,
                                 include_client_id=True)
            logging.info("Token retrieved successfully.")

            access_token = session.token
            with open(self.access_token_file, "wb") as file:
                # file.write(access_token)
                pickle.dump(access_token, file)
            return session

        except Exception as e:
            logging.error(f"Error fetching token: {e}")
            return None


