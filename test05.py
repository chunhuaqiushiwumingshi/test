# a=0
# b=1
# while b < 10000:

#     print(b,end=",")
#     a,b=b,a+b
# a = 1
# while a < 100:
#     if a%3 == 0:
#         print(a,"是3的整倍数")
#     else:
#         print(a,"不是3的整倍数")
#     a = a + 1
age = float(input("请输入猫的年龄:"))
if age <= 0:
    print("你在逗我吧！")
elif age <= 0.25:
    human = age * 24
    print("它的年龄相当于人类的",human,"岁。")
elif age <= 0.5:
    human = age * 20
    print("它的年龄相当于人类的",human,"岁。")
elif age <= 1:
    human = age * 15
    print("它的年龄相当于人类的",human,"岁。")
elif age > 1:
    human = age * 4 + 16
    print("它的年龄相当于人类的",human,"岁。")