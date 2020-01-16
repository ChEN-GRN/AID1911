"""
interest表,使用input输入一个学生的姓名,查找该学生的姓名,爱好,价格信息
"""
"""
数据库读取
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

# 读操作
sql='select name,age,score from cls01 where age>%s and score>%s;'




cur.execute(sql,[10,99])#执行sql语句
# cur.execute(sql)#执行sql语句
# 获取结果方法1

# for i in cur:
#     print(i)

# 获取结果方法2
# one_row=cur.fetchone()#获取一条记录
# print(one_row)
# 获取结果方法3
# many_row=cur.fetchmany(3)
# print(many_row)

# 获取结果方法4
# info=input("输入一个学生姓名:")
# for i in cur:
#     if info==i[0]:
#         print(i)



# all_row=cur.fetchall()
print(cur.fetchall())


# 关闭游标和数据库的链接
cur.close()

db.close()