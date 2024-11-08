# LinkedIn Profile Picture Saver

Цей проєкт використовує LinkedIn API для отримання даних профілю користувача та збереження профільного зображення. Перший раз користувач повинен пройти авторизацію через LinkedIn і надати посилання для підтвердження доступу. Далі програма зберігає доступ до LinkedIn API для повторного використання.

## Вимоги

- Python 3.x
- `requests`
- `requests_oauthlib`
- `logging`

### Встановлення залежностей

```
pip install requests requests_oauthlib
pip install requests logging
pip install requests requests
```

## Як це працює

Коли ви вперше запускаєте програму, вам потрібно буде перейти по посиланню, яке програма надає для авторизації. Після цього ви вставляєте URL-адресу з редиректу, і токен доступу зберігається для подальшого використання.

### Налаштування LinkedIn API

1. Зареєструйте додаток на [LinkedIn Developers](https://www.linkedin.com/developers/).
2. Отримайте ваш `Client ID`, `Client Secret` та вкажіть URL перенаправлення (redirect URI).
3. Збережіть ці дані в `config.py`:

   ```python
   # config.py
   ACCESS_TOKEN = ''
   CLIENT_ID = 'YOUR_CLIENT_ID'
   CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
   REDIRECT_URI = 'YOUR_REDIRECT_URI'
   ACCESS_TOKEN_FILE = 'access_token.pkl'
   LOG_FILE_NAME = 'app.log'
   PICTURE_FILE_NAME = 'profile_picture.jpg'
   ```

## Запуск проєкту

### Перший запуск

1. Запустіть програму:

   ```bash
   python main.py
   ```

2. Програма згенерує посилання для авторизації на LinkedIn.
3. Перейдіть за посиланням, надайте доступ до профілю, а потім скопіюйте та вставте URL-адресу з редиректу в термінал.
4. Токен буде збережено у файл, і сесія буде створена.

### Повторний запуск

При наступному запуску програма автоматично використовуватиме збережений токен для доступу до LinkedIn API, перевіряючи його на дійсність.

## Опис основних файлів

### main.py

- Завантажує токен доступу або ініціює нову авторизацію, якщо токен відсутній.
- Викликає функцію `get_profile_json()` для отримання JSON-даних профілю та `save_image_from_url()` для збереження зображення профілю.

### linkedin_token.py

- Клас `LinkedInToken` відповідає за створення OAuth2-сесії, збереження і перевірку дійсності токена.

### Основні функції

- **get_profile_json**: Запитує дані профілю користувача.
- **save_image_from_url**: Зберігає профільне зображення за URL-адресою в локальний файл.
- **LinkedInToken**: Клас для керування OAuth2-сесією, отримання та збереження токена.

## Логування

Програма веде логування у файл `out.log`, зберігаючи дані про успішність авторизації та обробки запитів.

## Примітки щодо reCAPTCHA

Цей проєкт використовує **офіційне API LinkedIn**, тому reCAPTCHA не передбачена та не потребує додаткових кроків для її обходу.

---
