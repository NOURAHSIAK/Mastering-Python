mainpassword = "kaisb@123"
inputpassword = input("enter your password: ")
tries = 5
while mainpassword != inputpassword:
    tries -= 1
    print(f"password is wrong, { "last" if tries == 0 else tries} tries left")
    inputpassword2 = input("write your password again: ")

    if tries == 0:
        print("your tries is finished")
        break
else:
    print ("correct passowrd")
