# c=2
# a =21
# c **= a
# print(c)
a0,a1,a2,a3,a4,a5,a6,a7,a8 = 1,2,4,8,16,32,64,128,256
b = input("请输入10进制的数值：")
b = int(b)
if b >511:
    print("输入数值过大，请输入512以内的数值")
else:
    
    c0 = b // a8
    b = b - c0 * a8
    c1 = b // a7
    b = b - c1 * a7
    c2 = b // a6
    b = b - c2 * a6
    c3 = b // a5
    b = b - c3 * a5
    c4 = b // a4
    b = b - c4 * a4
    c5 = b // a3
    b = b - c5 * a3
    c6 = b // a2
    b = b - c6 * a2
    c7 = b // a1
    b = b - c7 * a1
    c0,c1,c2,c3,c4,c5,c6,c7,b = str(c0),str(c1),str(c2),str(c3),str(c4),str(c5),str(c6),str(c7),str(b)
    print(c0+c1+c2+c3+c4+c5+c6+c7+b)
# a = 20
# b = 21
# c = b % a
# print(c)