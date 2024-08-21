class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("food is created from base class")

    def eat(self):
        print("eat method from base class")

class Apple(Food):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount
        print(f"{self.name} is created from derived class and price is {self.price} and amount is {self.amount}")
    

# food_one = Food("pizza", 6)
food_two = Apple("pizza", 150, 600)
food_two.eat()