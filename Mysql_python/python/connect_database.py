import pymysql
while True:
    username = input("用户名")
    pwd=input("密码")
    mobile =input("手机号")

    if username=='Q'or username=='q':
        break

    # 1.连接Mysql
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='1234',charset='utf8',database='unicom')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2.发送指令
    sql="insert into admin1(username,password,mobile) values (%s,%s,%s);"
    cursor.execute(sql,[username,pwd,mobile])
    conn.commit()  # 提交

    # sql="insert into admin1(username,password,mobile) values (%s,%s,%s);"
    # data=[('sxz1','123456','12345678901'),('sxz2','123456','12345678901'),('sxz3','123456','12345678901')]
    # cursor.executemany(sql,data)  # 批量插入

    # 3.关闭
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接