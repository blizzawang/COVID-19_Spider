import json

# 准备数据
py_list = [{'id': 1, 'first_name': 'Jeanette', 'last_name': 'Penddreth', 'email': 'jpenddreth0@census.gov', 'gender': 'Female', 'ip_address': '26.58.193.2'}, {'id': 2, 'first_name': 'Giavani', 'last_name': 'Frediani', 'email': 'gfrediani1@senate.gov', 'gender': 'Male', 'ip_address': '229.179.4.212'}, {'id': 3, 'first_name': 'Noell', 'last_name': 'Bea', 'email': 'nbea2@imageshack.us', 'gender': 'Female', 'ip_address': '180.66.162.255'}]

# Python数据转为json字符串
json_str = json.dumps(py_list,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将Python数据以json格式存入文件
with open('data/data2.json','w') as f:
    json.dump(py_list,f,ensure_ascii=False)

