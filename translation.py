import requests
import json
import apikey
API_URL = "https://api-inference.huggingface.co/models/t5-small"
headers = {"Authorization": f"Bearer {apikey.huggingkey}"}

def query(payload):
    payload = {"inputs": payload}
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    out =  json.loads(response.content.decode("utf-8"))
    return out[0]['translation_text']
	