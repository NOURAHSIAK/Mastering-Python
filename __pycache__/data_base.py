import sqlite3
db = sqlite3.connect("app.db")
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
#save (commit) changes
db.commit()
# close data base
db.close()
