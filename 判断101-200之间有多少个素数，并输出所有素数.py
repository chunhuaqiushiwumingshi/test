# #判断101-200之间有多少个素数，并输出所有素数
# a = 0
# for i in range(101,201):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         a +=1
# print(a)
i = int(input("请输入你的分数："))
if i >= 80:
    print("A")
elif i >= 60:
    print("B")
else:
    print("C")