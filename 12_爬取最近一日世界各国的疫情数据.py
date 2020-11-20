import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
# 发送请求，获取响应
response = requests.get(url)
content = response.content.decode()

# 提取最近一日世界各国的疫情数据
soup = BeautifulSoup(content, 'lxml')
script = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
text = script.get_text

# 从数据中心获取json字符串
json_str = re.findall(r'\[.*\]', str(text))[0]

# 将json字符串转为Python数据
data = json.loads(json_str)

# 将数据以json格式存入文件
with open('data/corona_virus_country_data.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False)
