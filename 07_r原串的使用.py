import re

rs = re.findall('a\nbc', 'a\nbc')
print(rs)

rs = re.findall('a\\\\nbc', 'a\\nbc')
print(rs)

# r原串
rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)
