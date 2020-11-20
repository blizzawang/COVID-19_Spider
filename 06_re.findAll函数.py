import re

# rs = re.findall('\d','a12b34c56')
# print(rs)

# rs = re.findall('\d+','a12b34c567')
# print(rs)

# flags参数的使用
# rs = re.findall('a.bc', 'a\nbc',re.DOTALL)
# print(rs)

# 分组
rs = re.findall('a.bc', 'a\nbc',re.DOTALL)
rs2 = re.findall('a(.)bc', 'a\nbc', re.DOTALL)
print(rs)
print(rs2)

