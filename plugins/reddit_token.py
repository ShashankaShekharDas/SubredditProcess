import requests
from airflow.models import Variable


def create_token():
    auth = requests.auth.HTTPBasicAuth('-pokI4HzWE1aiK7-fNKz3w', 'a7dbIisvYew3FBSROUY829lBi4Xldg')
    data = {'grant_type': 'password',
            'username': Variable.get("reddit_username"),
            'password': Variable.get("reddit_password")}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json()['access_token']
    Variable.set("reddit_token", token)
    print(token)
    return token

if __name__ == "__main__":
    create_token()