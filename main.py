import requests
import os

BASE_URL = "https://api.openai.com/v1"
MODELS_URL = "%s/models" % BASE_URL
API_KEY = os.environ.get('API_KEY')


def call_open_ia():
    headers = {
        f"Authorization": f"Bearer {API_KEY}",
    }

    response = requests.get(MODELS_URL, headers=headers)

    print(response.json())

    for i in response.json()["data"]:
        print(i["id"])


if __name__ == '__main__':

    call_open_ia()

