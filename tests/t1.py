import pymysql;
db = pymysql.connect("localhost", "root", "123456", "iotplatform")
cursor = db.cursor()
try:
    cursor.execute("select user_ID, location, time from share order by ID desc")
    temp = cursor.fetchall()
    db.commit()
except:
    db.rollback()
db.close()
#print(temp[1]);
#sharelist = [];
re = {'list': []}
for i in range(len(temp)):
    re['list'].append({'user_ID': temp[i][0], 'location': temp[i][1]});
print(re['list'][0]);
#print(temp)
#d = {'a': 1}
#print(d['a'])
#a = {'f': temp[0][0]}
#print(a['f'])
#b = {'f': temp[1][2]}
#print(b['f'])
#d = {'a': {'b': 1}, 'c': {'b': 2}}