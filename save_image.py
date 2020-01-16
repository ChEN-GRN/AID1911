"""
存取二进制文件
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

# 存储图片
# with open('/home/tarena/桌面/timg.jpeg','rb') as f:
#     data= f.read()
# try:
#     sql="update cls01 set image=%s where name='利国';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception:
#     db.rollback()

#获取图片
sql="select image from cls01 where name='利国';"
cur.execute(sql)
data=cur.fetchone()
print(data)
with open('张曼玉.jpeg','wb') as f:
    f.write(data[0])



# 关闭游标和数据库的链接
cur.close()

db.close()
