list = [1, 2, 3, 4, 5]
dict = {"name" : "kais", "age" : 36, "country" : "Tunisia"}

for num in list:
    print(num)

for key, value in dict.items():
    print(f"{key} ==> {value}")

def name_star():
    print("hello form start")
name_star()