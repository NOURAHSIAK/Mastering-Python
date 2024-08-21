class Member:
    def __init__(self, name):

        self.__name = name #private

    def say_hello(self):

        return f"hello {self.name}"

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

one = Member("ahmed")
print(one.get_name())
one.set_name("sayed")
print(one.get_name())
