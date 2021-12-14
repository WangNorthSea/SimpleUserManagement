import pymysql

# 连接配置信息
conn = pymysql.connect(host='127.0.0.1',
                       port = 3306,
                       user = 'root',
                       password = 'wjwhy1998',
                       db = 'seproject',
                       charset = 'utf8')

# 创建连接
cur = conn.cursor()
cur.execute("SELECT * from users")
for r in cur:
    print(r)
cur.close()
conn.close()