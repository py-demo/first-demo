# coding:utf-8
# python-3.6

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

# 创建游标
cur = conn.cursor()

try:
    # Create a new record
    sql = "INSERT INTO `user`() VALUES (null, %s, %s)"
    cur.execute(sql,('saturn2', 'saturn2.eich'))
    conn.commit()

    # Read a single record
    sql = "SELECT * FROM `user`"
    cur.execute(sql)

    # result = cur.fetchone()
    # result = cur.fetchmany(2)
    result = cur.fetchall()
    print(result)
finally:
    cur.close()
    conn.close()
