import usermodule

user = usermodule.UserModule()
dbreturn = user.register('beihai', '123456')
print(dbreturn)

dbreturn = user.register('beihai', '123456')
print(dbreturn)

dbreturn = user.login('beihai', '123456')
print(dbreturn)

dbreturn = user.login('beihai', '123')
print(dbreturn)

dbreturn = user.delete('beihai')
print(dbreturn)