
import dbutil as db

sql = "insert into users(name, password) values('xianzhong', 'asdf')"
result = db.db_execute(sql)

sql = "select * from users"
result = db.db_execute(sql)
print(result)

sql = "delete from users where name = 'xianzhong'"
result = db.db_execute(sql)

sql = "select * from users"
result = db.db_execute(sql)
print(result)