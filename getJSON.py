
import requests
import json

def getJSON(url,apiHost):
    apiKey = "762b5d224dmshf42d5d9897e6317p13aa11jsn1b5eb6b7d725"
    # Set the headers
    headers = {
    "X-Rapidapi-Key": apiKey,
    "X-Rapidapi-Host": apiHost
    }
    response = requests.get(url,headers=headers)
    return response.json()
