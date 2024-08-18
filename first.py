myfavoriteswebs = []
maximumwebs = 5 
while maximumwebs > 0:
    webs = input("website name without https//: ")
    myfavoriteswebs.append(f"https//{webs.strip().lower()}")
    maximumwebs -= 1
    print(f"website added, {maximumwebs} places left" )
    print(myfavoriteswebs)
else:
    print("bookmark is full you can't add more")
if len(myfavoriteswebs) > 0:
    myfavoriteswebs.sort()
    index = 0
    print("printing the websites in your bookmark")
    while index < len(myfavoriteswebs):
        
        print(myfavoriteswebs[index])
        index += 1
