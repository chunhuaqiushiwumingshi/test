# i = 1
# j = 1
# while j <= 9:
#     i = (i+1)*2
#     j +=1
# print("猴子摘了",i,"个桃")
# from tkinter import N


# i = "*"
# j = " "
# n = 1
# while n <=5:
#     print(j*(5-n),i*(2*n-1))
#     n +=1
# while n <=9:
#     print(j*(n-5),i*(2*(9-n)+1))
#     n +=1



i,j,k,count  = 2,1,1,0
while k <=20:
    count += i/j
    i,j = i+j,i
    k += 1
    print(count)
print("count =",count)