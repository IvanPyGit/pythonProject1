import time
import jwt
import requests


service_account_id = "ajeklj8oib9gq34dh9sn"
key_id = "ajeoa28hhkmjc4hp0268" # ID ресурса Key, который принадлежит сервисному аккаунту.


with open("private.pem", 'r') as private:
    private_key = private.read()

now = int(time.time())
payload = {
        'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        'iss': service_account_id,
        'iat': now,
        'exp': now + 360}

# Формирование JWT.
encoded_token = jwt.encode(
    payload,
    private_key,
    algorithm='PS256',
    headers={'kid': key_id})
print(encoded_token)

headers = {
    'Content-type': 'application/json',
}

data = '{"jwt": "<SIGNED-JWT>"}'


response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', headers=headers, json=data)

print(response)