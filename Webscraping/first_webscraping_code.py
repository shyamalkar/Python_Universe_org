

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"

response = requests.get(url)

print(response.status_code)
print(response.text)





