import requests


class Client:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.googleapis.com/youtube/v3/"


    def _get(self, params):
        response = requests.get(url=self.url, params=params)
        return response


class SearchVideo:

    def __init__(self, keyword, api_key):
        self.keyword = keyword
        self.api_key = api_key
        self.url_add = "search"

    def search(self):
        client = Client(self.api_key)
        client.url = client.url + self.url_add
        print("client.url: ", client.url)                   # delete
        params = {
            "maxResults" : 25,
            "part" : "snippet",
            "key" : self.api_key,
            "q" : self.keyword}

        print("params: ", params)                           # delete

        data = client._get(params=params)
        print("data: ", data)                               # delete
        return data

