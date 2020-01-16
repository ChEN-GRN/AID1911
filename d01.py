"""
mysql.py
pymsql的基本流程
"""
import pymysql
# 链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur=db.cursor()

# 执行各种sql操作




# 关闭游标和数据库的链接
cur.close()

db.close()
#也是放弃 才能靠近你
