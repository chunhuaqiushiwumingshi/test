# a,b = 0,1
# while a <= 1000:
#     print(a,end=',')
#     a,b = b,a+b
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and j != k and k != i :
#                 count += 1
#                 print(i*100+j*10+k)
# print(count)
from re import M


# a = 2   #初始兔子数量
# n = 10  #请输入时间（单位月）
# i,j,k = 0,0,a
# m = 0

# while m <= n:
#     print(k,end=',')
#     i,j,k = j,k,i+k
#     m += 1

i = int(input("请输入你的销售业绩："))
if i > 1000000:
    end = (i-1000000)*0.01 + 400000*0.015 + 200000*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
    print("你的提成是",end,"元")
elif i > 600000:
    end = (i-600000)*0.015 + 200000*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
    print("你的提成是",end,"元")
elif i > 400000:
    end = (i-400000)*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
    print("你的提成是",end,"元")
elif i > 200000:
    end = (i-200000)*0.05 + 100000*0.075 + 100000*0.1
    print("你的提成是",end,"元")
elif i > 100000:
    end = (i-100000)*0.075 + 100000*0.1
    print("你的提成是",end,"元")
else:
    end = i*0.1
    print("你的提成是",end,"元")