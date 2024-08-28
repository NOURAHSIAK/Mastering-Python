import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()
def commit_close():
    #save (commit) changes
    db.commit()
    # close data base
    db.close()
    print("connection to data base is closed")
#user id
uid = 1
input_message = """
what do you want to do ?
"s" => show all skills
"a" => add new skills
"d" => delete a skill
"u" => update skill progress
"q" => quit the app
Choose option:  
"""
user_input = input(input_message).strip().lower()
# command list
commands_list = ["s", "a", "d", "u", "q"]
# define the method
def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    results = cr.fetchall()
    print(f"you have {len(results)} skills")
    if len(results) > 0:
        print("showing your skills with progress: ")
    for row in results:
        print(f"skill => {row[0]}", end=" ")
        print(f"progress => {row[1]}%")
    commit_close()
def add_skill():
    sk = input("write skill name: ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    results = cr.fetchone()
    if results == None:
        prog = input("write skill progress: ").strip()
        cr.execute(f"insert into skills (name, progress, user_id) values ('{sk}', '{prog}', '{uid}')")
    else:

        x = input("you cannot add it, do you want to update progress, yes/no: ").lower().strip()
        if x == "yes":
            prog = input("write new progress for your skill: ").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

    commit_close()
def delete_skill():
    sk = input("write skill name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_close()
def update_skill():
    sk = input("write skill name: ").strip().capitalize()
    prog = input("write new skill progress: ").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    commit_close()

# check if commands is exist
if user_input in commands_list:
    print(f"commands found {user_input}")
    if user_input == "s":
        show_skills()
        
    elif user_input == "a":
        add_skill()
        
    elif user_input == "d":
        delete_skill()
        
    elif user_input == "u":
        update_skill()
        
    else:
        print("app is closed")
        commit_close()
else:
    print(f"sorry this commands \"{user_input}\" is not found")