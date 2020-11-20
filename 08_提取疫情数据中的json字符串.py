import re
import requests
from bs4 import BeautifulSoup

# 数据来源
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
# 发送请求，获取响应内容
response = requests.get(url)
# 解决中文乱码问题
content = response.content.decode()
# 使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(content, 'lxml')
# 获取script标签
script = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
# 获取script标签的文本内容
text = script.get_text
# print(text)
# 使用正则表达式提取json字符串
json = re.findall(r'\[.+\]', str(text))[0]
print(json)
