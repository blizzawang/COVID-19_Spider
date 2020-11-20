import re

# 字符匹配
# rs = re.findall('abc', 'abc')
# rs2 = re.findall('abc', 'adc')
# print(rs)
# print(rs2)

# .匹配
# rs = re.findall('a.c','abc')
# rs2 = re.findall('a.c','a&c')
# rs3 = re.findall('a.c','a\nc')
# rs4 = re.findall('a.c','aadsacacc')
# print(rs)
# print(rs2)
# print(rs3)
# print(rs4)

# 转义匹配
# rs = re.findall('a\.c', 'a.c')
# print(rs)

# 字符集匹配
# rs =re.findall('a[bc]d','abd')
# rs2 =re.findall('a[bc]d','acd')
# rs3 =re.findall('a[bc]d','add')
# print(rs)
# print(rs2)
# print(rs3)

# 预定义字符集匹配
# rs = re.findall('a[\d]b', 'a1b')
# rs2 = re.findall('a[\d]b', 'aab')
# print(rs)
# print(rs2)

# rs = re.findall('a[\w]c','a1c')
# rs2 = re.findall('a[\w]c','abc')
# rs3 = re.findall('a[\w]c','aZc')
# rs4 = re.findall('a[\w]c','a#c')
# rs5 = re.findall('a[\w]c','a中c')
# print(rs)
# print(rs2)
# print(rs3)
# print(rs4)
# print(rs5)

# 数量词*匹配
# rs = re.findall('a[\d]*c','ac')
# rs2 = re.findall('a[\d]*c','a1c')
# rs3 = re.findall('a[\d]*c','a1234567c')
# print(rs)
# print(rs2)
# print(rs3)

# 数量词+匹配
# rs = re.findall('a[\d]+c','ac')
# rs2 = re.findall('a[\d]+c','a1c')
# rs3 = re.findall('a[\d]+c','a1234567c')
# print(rs)
# print(rs2)
# print(rs3)

# 数量词?匹配
# rs = re.findall('a[\d]?c','ac')
# rs2 = re.findall('a[\d]?c','a1c')
# rs3 = re.findall('a[\d]?c','a1234567c')
# print(rs)
# print(rs2)
# print(rs3)

# 数量词m匹配
rs = re.findall('a[\d]{0}c','ac')
rs2 = re.findall('a[\d]{1}c','a1c')
rs3 = re.findall('a[\d]{2}c','a1234567c')
rs4 = re.findall('a[\d]{7}c','a1234567c')
print(rs)
print(rs2)
print(rs3)
print(rs4)