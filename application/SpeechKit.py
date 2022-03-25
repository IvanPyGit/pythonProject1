import urllib.request
import configparser
import json


"""Функция перевода аудио (русская речь) в текст"""
# забираем авторизационные данные из файла
config = configparser.ConfigParser()
config.read('yandex_config.ini')
API_KEY = config['CREDENTIALS']['authorization_API']
id_catalog = config['ULR']['id_catalog']
URL = config['ULR']['URL']
# в поле заголовка передаем IAM_TOKEN:
headers = f'Authorization: Api-Key {API_KEY}'
# остальные параметры для POST запроса:
params = "&".join([
    "topic=general",
    "folderId=%s" % id_catalog,
    "lang=ru-RU"
])
with open("speech.pcm", "rb") as f:
    data = f.read()

def get_post_SpeechKit():
    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % API_KEY)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)
    if decodedData.get("error_code") is None:
        print(decodedData.get("result"))


print(get_post_SpeechKit())

