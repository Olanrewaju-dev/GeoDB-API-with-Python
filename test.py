import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


url = os.getenv("myURL")

headers = {
	"X-RapidAPI-Key": os.getenv("RapidAPIKey"),
	"X-RapidAPI-Host": os.getenv("RapidAPIHost")
	}

response = requests.request("GET", url, headers=headers)

print(response.status_code)
print(json.dumps(response.json(), indent=2))