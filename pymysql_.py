# coding:utf-8

import pymysql.cursors

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'db': 'py_db',
    'charset': 'utf8mb4'
}

# 创建连接
conn = pymysql.connect(**config)

try:
    with conn.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `user`() VALUES (null, '%s', '%s')" % ('saturn', 'saturn.eich')
        sql = "INSERT INTO `address`() VALUES (null, '%s', '%s')" % ('8', 'saturn@qq.com')
        # cursor.execute(sql)

        # conn.commit()

    with conn.cursor() as cursor:
        # Read a single record
        # sql = "SELECT * FROM `user`"
        sql = "SELECT user_id,a.id,name,email FROM `address` as a,`user` as b WHERE a.user_id=b.id"
        cursor.execute(sql)

        result = cursor.fetchone()
        print(result)
finally:
    conn.close()