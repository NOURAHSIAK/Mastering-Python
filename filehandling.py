
# myfile = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\kais.txt", "w")
# myfile.write("hello python\n\n\n")

# mylist = ["osama\n", "mansour\n", "walid\n"]

# myfile = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\fun.txt", "w")
# myfile.writelines(mylist)

# myfile = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\kais.txt", "a")
# myfile.write("this is new line")
# myfileone = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\kais.txt","r")
# # print(myfileone)
# # print(myfileone.read())
# # print(myfileone.readline(3))
# # print(myfileone.readline())
# # print(myfileone.readline())
# myfile = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\kais.txt", "a")
# myfile.truncate(5)
# print(myfile.tell())
myfile = open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\kais.txt", "r")
myfile.seek(13)
print(myfile.read())
