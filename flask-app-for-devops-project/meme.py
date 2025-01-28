import requests
import json

class Meme:
    def __init__(self):
        pass

    def getMeme(self):
        url = "https://meme-api.com/gimme"
        response = json.loads(requests.request("GET", url).text)
        meme_large = response["preview"][-2]
        subreddit = response["subreddit"]
        return meme_large, subreddit