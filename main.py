import requests


class Client:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.googleapis.com/youtube/v3/"


    def _get(self, params):
        response = requests.get(url=self.url, params=params)
        return response


