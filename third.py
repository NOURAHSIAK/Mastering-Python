# skills = { "html": "60%", "css" : "70%", "php" : "90%"}
# for skill in skills:
#     print(f"my progrsse in the lang {skill} is {skills[skill]}")
students = {
    "osama" : { "css" : "50%", "html": "40%", "js":"70%"},
    "ali" : { "css" : "50%", "html": "40%", "js":"70%"},
    "walid" : { "css" : "50%", "html": "40%", "js":"70%"}
}

for name in students:
    print(f"skills progress of {name} is: ")
    for skill in students[name]:
        print(f"{skill} => {students[name][skill]}")