import requests


class Client:

    url = "https://www.googleapis.com/youtube/v3"
    
    def __init__(self, api_key):
        self.api_key = api_key


    def get(self, url, **params):
        response = requests.get(url=url, params=params)
        return response