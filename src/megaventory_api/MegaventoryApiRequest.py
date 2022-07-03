import requests
import json
from src.model.ConfigFile import ConfigFile


class MegaventoryApiRequest:

    def __init__(self, configFile, urlPath="", method="POST"):
        self.apiKey = configFile.get('GENERAL', 'api_key')
        self.url = configFile.get('GENERAL', 'api_url') + "/" + urlPath
        self.method = method.upper()
        self.request = {
            'APIKEY': self.apiKey
        }

    def getRequest(self):
        return self.request

    def appendToRequest(self, key, value):
        self.request[key] = value


    def sendRequestPost(self):
        return requests.post(url=self.url, json=self.request).json()


    def sendRequestGet(self):
        return requests.get(url=self.url, json=self.request).json()


    def sendRequest(self):

        if self.method == "POST":
            return self.sendRequestPost()
        elif self.methon == "GET":
            return self.sendRequestGet()
        else:
            raise Exception("Method not supported")

    
