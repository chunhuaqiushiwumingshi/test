# a = [1,21,4342,-2,212,-23,40,100]
# b = len(a)
# for j in range(b):
#     for i in range(0,b-j-1):
#         if a[i] > a[i+1]:
#             t = a[i]
#             a[i] = a[i+1]
#             a[i+1] = t
#             print(a)
# print(a)
a = [1,21,4342,-2,212,-23,40,100]
b = len(a)
for j in range(b):
    for i in range(0,b-1):
        if a[i] > a[j]:
             t = a[i]
             a[i] = a[j]
             a[j] = t
             print(a)