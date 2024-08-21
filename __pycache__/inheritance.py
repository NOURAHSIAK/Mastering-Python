class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("food is created from base class")

    def eat(self):
        print("eat method from base class")

class Apple(Food):
    def __init__(self):
        print("apple is created from derived class")
    

food_one = Food("pizza", 6)
food_two = Apple()
food_two.eat()