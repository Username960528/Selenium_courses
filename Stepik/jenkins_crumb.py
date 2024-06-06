import requests
from requests.auth import HTTPBasicAuth

# Ваши учетные данные Jenkins
username = 'tribe'
api_token = '11e2f327c89d370d7d5256a1053dfd5bf0'

# URL для получения crumb
url = 'http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'

# Выполнение запроса с аутентификацией
response = requests.get(url, auth=HTTPBasicAuth(username, api_token))

# Проверка ответа
if response.status_code == 200:
    crumb_data = response.text
    print('Crumb data:', crumb_data)
else:
    print('Failed to get crumb:', response.status_code)
    print('Response:', response.text)