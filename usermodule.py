
import dbutil as db

dbctrl = db.DBController()

sql = "insert into users(name, password) values('xianzhong', 'asdf')"
result = dbctrl.db_execute(sql)

sql = "select * from users"
result = dbctrl.db_execute(sql)
print(result)

sql = "delete from users where name = 'xianzhong'"
result = dbctrl.db_execute(sql)

sql = "select * from users"
result = dbctrl.db_execute(sql)
print(result)