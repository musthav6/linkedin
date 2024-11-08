import requests
from config import ACCESS_TOKEN,LOG_FILE_NAME,PICTURE_FILE_NAME, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN_FILE, REDIRECT_URI
import logging
import urllib.request
from linkedin_token import LinkedInToken
from requests_oauthlib import OAuth2Session

logging.basicConfig(filename=LOG_FILE_NAME, level=logging.INFO, format='%(asctime)s - %(message)s')


def get_profile_json(session):
    # headers = {
    #     'Authorization': f'Bearer {token}',
    #     'Connection': 'Keep-Alive'
    # }
    try:
        profile_url = "https://api.linkedin.com/v2/userinfo"
        # response = requests.get(profile_url, headers=headers)
        response = session.get(profile_url)

        profile_data = response.json()
        if response.status_code == 200:
            logging.info("Profile data retrieved successfully")
            return profile_data
        else:
            logging.info(f"Profile data is not retrieved successfully{response.text, response.status_code}:",)
            return {'status':'failed'}
    except Exception as e:
        logging.error(f"in get_profile_json func:{e}")
        return None


def save_image_from_url(url, filename):
    urllib.request.urlretrieve(url, filename)


if __name__ == "__main__":
    linked_in = LinkedInToken(client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET,
                              access_token_file=ACCESS_TOKEN_FILE,
                              redirect_uri=REDIRECT_URI)

    if linked_in.token_validated():
        print('You are authorised to work with API. Lets save the picture')
        token = linked_in.load_token()
        session = OAuth2Session(client_id=CLIENT_ID,redirect_uri=REDIRECT_URI,token=token)

    else:
        print('It is your first registration. We need to get a new session to work with API')
        session = linked_in.get_session()


    profile_json = get_profile_json(session)
    picture_url = profile_json['picture']
    logging.info("Profile url retrieved successfully")

    save_image_from_url(url=picture_url, filename=PICTURE_FILE_NAME)
    logging.info("Profile picture saved successfully")
    print('Image saved successfully')