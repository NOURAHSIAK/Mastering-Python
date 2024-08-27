#import sqlite module
import sqlite3
# create data base and connect
db = sqlite3.connect("app.db")
#setting up the cursor
cr = db.cursor()
# create the tables and fields
cr.execute("create table if not exists users(user_id integer, name text)")
cr.execute("create table if not exists skills(name text, progress integer, user_id integer)")
#inserting data
# cr.execute("insert into users(user_id, name) values(1, 'ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'ali')")
# cr.execute("insert into users(user_id, name) values(3, 'amir')")
my_list = ["ali", "osama", "dali", "mona"]
for key, user in enumerate(my_list):
    cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")
# update data
cr.execute("update users set name = 'mahmoud' where user_id = 1")
cr.execute("update users set name = 'ossama' where user_id = 2")
cr.execute("update users set name = 'halim' where user_id = 3")
# delete data
cr.execute("delete from users where user_id = 3")
# fetch data
cr.execute("select * from users")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
#save (commit) changes
db.commit()
# close data base
db.close()
