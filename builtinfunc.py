mylist = ["osama", "ali", "adem"]
x = map(lambda name: f"-{name.strip().capitalize()}-", mylist)
for name in list(x):
    print(name)