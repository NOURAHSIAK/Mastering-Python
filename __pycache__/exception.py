the_file = None
tries = 5
while tries > 0:
    try:
        print(f"you have {tries} left")
        file_path = input("enter the file path: ").strip()
        the_file = open(file_path, "r")
        print(the_file.read())


    except FileNotFoundError:
        print("your file name is not valid")
        tries -= 1
    except:
        print("error happened")

    finally:
        if the_file is not None:
            the_file.close()
            print("file closed")



else:
    print("all tries is finished")