# skillsun = {"csss":"50%", "phhp": "80%"}
# skill_tuple = ("html", "css")
# def show_skills(name, *skills, **skillsprog):
#     print(f"show {name} skills without rpogress")
#     for skill in skills:
#         print(skill)
#     print(f"show {name} skills with progress")
#     for keys, value in skillsprog.items():
#         print(f"{keys} => {value}")

# show_skills("kais", *skill_tuple, **skillsun)
word = "wwwooorrlldd"
def word_format(wrd):
    if len(wrd) == 1:
        return wrd
    if wrd[0] == wrd[1]:
        return word_format(wrd[1:])
    return wrd[0] + word_format(wrd[1:])
print(word_format(word))
word_format(word)