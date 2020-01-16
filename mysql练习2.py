"""
将dict.txt 文件中所有单词存入这个数据表
注意后面操作为频繁的查询语句
"""

import pymysql
import re
# 链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')
# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur=db.cursor()

# 执行各种sql操作
fd=open('dict.txt','r')


args_list=[]
for line in fd:
    l=re.findall(r'(\w+)\s+(.*)',line)
    print(l)
    args_list.extend(l)
sql="insert into words (word,mean) values (%s,%s)"
try:
    cur.executemany(sql,args_list)
    db.commit()
except Exception:
    db.rollback()
# 关闭游标和数据库的链接
cur.close()

db.close()