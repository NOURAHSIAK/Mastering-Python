import sqlite3
db = sqlite3.connect("app.db")
cr = db.Cursor()
def commit_close():
    #save (commit) changes
    db.commit()
    # close data base
    db.close()
    print("data base is closed")
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
    pass
    commit_close()
def add_skill():
    sk = input("write skill name: ").strip().capitalize
    prog = input("write skill progress: ").strip()
    cr.execute(f"insert into skills (name, progress, user_id) values ('{sk}', '{prog}', '{uid}')")
    commit_close()
def delete_skill():
    pass
    commit_close()
def update_skill():
    pass
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
else:
    print(f"sorry this commands \"{user_input}\" is not found")