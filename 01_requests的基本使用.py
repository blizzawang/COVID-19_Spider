import requests

# 发送请求，获取响应
response = requests.get('http://www.baidu.com')

# 获取编码格式
# print(response.encoding)
# 设置编码格式
response.encoding = 'utf8'
# 得到数据
print(response.text)
# response.content获取二进制数据，并通过decode指定解码格式进行解码
# print(response.content.decode('utf8'))
