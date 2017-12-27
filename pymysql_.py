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
        sql = "INSERT INTO `user`() VALUES (null, '%s', '%s')" % ('saturn', 'saturn.eich')
        cursor.execute(sql)

    # conn.commit()

    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `user`"
        cursor.execute(sql)

        result = cursor.fetchone()
        print(result)
finally:
    conn.close()