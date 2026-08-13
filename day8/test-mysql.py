#
# import pymysql
#
# con = pymysql.Connection(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='zb061128',
#     autocommit=True,
# )
#
# print(con.get_server_info())
#
# cur = con.cursor()
# con.select_db('test01')
# cur.execute("select * from student")
# result = cur.fetchall()
# print(result)
#
# con.close()
import json

f = open("C:\\Users\\ZhuanZ\\Desktop\\test02.txt", "w")
l = list()
s1 = dict()
s1['name'] = "张三"
s1["age"] = 18
s1["gender"] = "male"
s2 = dict()
s2['name'] = "张三"
s2["age"] = 18
s2["gender"] = "male"
l.append(s1)
l.append(s2)
print(l)
j = json.dumps(l, ensure_ascii=False)
print(j)
f.write(j)
f = open("C:\\Users\\ZhuanZ\\Desktop\\test02.txt", "r")
j1 = f.read()
j2 = json.loads(j1)
print(j2)
print(type(j2))

