# def test():
#     print("这是yiled之前")
#     yield
#     # return True
#     print("这是yiled之后")
#     yield
#     print("我是猪")
    
# a = test()
# try:
#     next(a)
#     next(a)
#     next(a)
#     next(a)
# except:
#     exit()
# x = (i for i in range(10))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

class Person:
    name = "胡一凡"
    @classmethod
    def drink(cls):
        print(cls.name)
        print(Person.name)
        print("我要吃饭")

    def eat(self):
        self.food = "我要吃馒头"
        print("我要吃咸菜！")

person = Person()
person.eat()
print(person.food)