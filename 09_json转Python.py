import json

# 将json字符串转为Python数据
json_str = '''[{
  "id": 1,
  "first_name": "Jeanette",
  "last_name": "Penddreth",
  "email": "jpenddreth0@census.gov",
  "gender": "Female",
  "ip_address": "26.58.193.2"
}, {
  "id": 2,
  "first_name": "Giavani",
  "last_name": "Frediani",
  "email": "gfrediani1@senate.gov",
  "gender": "Male",
  "ip_address": "229.179.4.212"
}, {
  "id": 3,
  "first_name": "Noell",
  "last_name": "Bea",
  "email": "nbea2@imageshack.us",
  "gender": "Female",
  "ip_address": "180.66.162.255"
}]'''
# rs = json.loads(json_str)
# print(type(rs))
# print(rs)

# 将json格式的文件转为Python数据
with open('data/data.json') as f:
    py_list = json.load(f)
    print(type(py_list))
    print(py_list)