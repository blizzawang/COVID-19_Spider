import requests
from bs4 import BeautifulSoup

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
response.encoding = 'utf8'
print(response.text)