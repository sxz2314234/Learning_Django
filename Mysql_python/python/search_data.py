import pymysql

# 1.连接Mysql
conn=pymysql.connect(host='localhost',port=3306,user='root',password='1234',charset='utf8',database='unicom')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令
# 删除与修改主要就是sql语句不同
sql="select * from admin1;"
cursor.execute(sql) 
data_list=cursor.fetchall()  # 获取所有数据，查询不用commit
# 打印数据
for row_data in data_list:
    print(row_data)
'''
res=cursor.fetchone() // 获取满足条件的一条数据
'''
# 3.关闭
cursor.close()  # 关闭游标
conn.close()  # 关闭连接