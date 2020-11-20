from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p class="title">
        <b>The title</b>
    </p>
    <p class="content">
        <a href="#" class="show" id="link1">zhanfsan</a>
        <a href="#" class="show" id="link2">lisi</a>
        <a href="#" class="show" id="link3">wangwu</a>
    </p>
    <p class="bottom">The bottom</p>
</body>
</html>'''
# 创建BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# 查找title标签
title = soup.find('title')
print(title)

# 查找a标签，find函数只能获取到第一个查找到的a标签
a = soup.find('a')
# 获取到的a是一个tag对象，通过该对象可以获取标签的一些信息
# print(a.name)  # 获取标签名
# print(a.attrs)  # 获取标签属性
# findAll函数能获取到所有的标签
# a = soup.findAll('a')
# print(a)

# 根据属性进行查找
# 查找id为link1的标签
# 通过命名参数进行指定
link1 = soup.find(id='link1')
# print(link1)
# 使用attrs指定属性字典
link2 = soup.find(attrs={'id': 'link2'})
# print(link2)

# 根据文本进行查找
text = soup.find(text='wangwu')
print(text)

