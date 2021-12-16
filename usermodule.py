
import hashlib
import dbutil
import uuid

class UserModule:

    def __init__(self):
        self.db = dbutil.DBController()

    def finduser(self, name):
        sql = "select * from users where name = \'" + name + "\'"
        result = self.db.db_execute(sql)
        if result == False:
            return False
        return result

    def register(self, name, password):
        find_result = self.finduser(name)
        if find_result == False:
            return "0 database error"
        if find_result:
            return "0 user has been registered"
        md5pw = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        sql = "insert into users(name, password) values(\'" + name + "\', \'" + md5pw + "\')"
        result = self.db.db_execute(sql)
        if result == False:
            return "0 database error"
        else:
            return "1 registration succeeded"

    def login(self, name, password):
        find_result = self.finduser(name)
        if find_result == False:
            return "0 database error"
        if find_result == ():
            return "0 wrong user name or password"
        md5pw = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        if md5pw == find_result[0][1]:
            return "1 " + str(uuid.uuid4())
        else:
            return "0 wrong user name or password"

    def delete(self, name):
        sql = "delete from users where name = \'" + name + "\'"
        result = self.db.db_execute(sql)
        if result == False:
            return "0 database error"
        else:
            return "1 delete succeeded"
