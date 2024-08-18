from time import time
#  def decorator(func):
#     def nestedfunc(*numbers):
#         for number in numbers:
#             if number <0:
#                 print("pay attention neg number")
#         func(*numbers)
#     return nestedfunc
# # @decorator
# # def sayhello():
# #     print("hello from sayhello func")
# # print("#" * 50)
# # @decorator
# # def sayhowreyou():
# #     print("how re you")
# @decorator
# def calc(num1, num2, num3, num4):
#     print(num1 + num2 + num3 + num4)
# calc(-19, 80, 20 , -4)

def speedtest(func):
    def nestedfunc():
        start = time()
        func()
        end = time()
        print(f"runing time is {end - start}")
    return nestedfunc
@speedtest
def bigloop():
    for n in range(1, 20000):
        print(n)
bigloop()
