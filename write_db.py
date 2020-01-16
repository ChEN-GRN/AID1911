
"""
mysql写操作
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
l=[('Dave',17,'M',94),('Ala',18,'W',44),('Eva',19,'M',94)]
sql="insert into cls01 (name,age,sex,score) values (%s,%s,%s,%s)"

try:
    # for i in l:
    #     cur.execute(sql,i)
    print(cur.executemany(sql,l))
    db.commit()
except Exception:
    db.rollback()#数据库回滚

# try:
#     sql="updatae cls01 set sex='m' where name='jame';"
#     cur.execute(sql)
#     sql="deltet from cls01 where sex is null;"
#     cur.execute(sql)
#     db.commit()
# except Exception:
#     db.rollback()



# 关闭游标和数据库的链接
cur.close()

db.close()