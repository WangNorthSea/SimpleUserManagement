
import hashlib
import dbutil
import uuid
import http.client
import json

class UserModule:

    def __init__(self):
        self.db = dbutil.DBController()
        self.return_format = {
            'result'    :   '',
            'reason'    :   '',
            'token'     :   ''
        }

    def construct_return(self, resultval, reasonstr, tokenstr):
        self.return_format['result'] = resultval
        self.return_format['reason'] = reasonstr
        self.return_format['token'] = tokenstr
        return self.return_format

    def finduser(self, name):
        sql = "select * from users where name = \'" + name + "\'"
        result = self.db.db_execute(sql)
        if result == False:
            return False
        return result

    def register(self, name, password):
        find_result = self.finduser(name)
        if find_result == False:
            return json.dumps(self.construct_return(False, "database error", ''))
        if find_result:
            return json.dumps(self.construct_return(False, "user has been registered", ''))
        md5pw = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        sql = "insert into users(name, password) values(\'" + name + "\', \'" + md5pw + "\')"
        result = self.db.db_execute(sql)
        if result == False:
            return json.dumps(self.construct_return(False, "database error", ''))
        else:
            return json.dumps(self.construct_return(True, "registration succeeded", ''))

    def login(self, name, password):
        find_result = self.finduser(name)
        if find_result == False:
            return json.dumps(self.construct_return(False, "database error", ''))
        if find_result == ():
            return json.dumps(self.construct_return(False, "wrong username or password", ''))
        md5pw = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        if md5pw == find_result[0][1]:
            conn = http.client.HTTPConnection("localhost:8000")
            uuidstr = str(uuid.uuid4())
            poststr = "/append?uuid=" + name + "&token=" + uuidstr
            conn.request("POST", poststr)
            res = conn.getresponse()
            content = res.read()
            #print("status=", res.status, "content=", content)
            conn.close()
            if res.status == 200 and content == bytes("Map Received", "ascii"):
                return json.dumps(self.construct_return(True, "login succeeded", uuidstr))
            else:
                return json.dumps(self.construct_return(False, "login failed because of server error", ''))
        else:
            return json.dumps(self.construct_return(False, "wrong username or password", ''))

    def delete(self, name):
        sql = "delete from users where name = \'" + name + "\'"
        result = self.db.db_execute(sql)
        if result == False:
            return json.dumps(self.construct_return(False, "database error", ''))
        else:
            return json.dumps(self.construct_return(True, "delete succeeded", ''))
