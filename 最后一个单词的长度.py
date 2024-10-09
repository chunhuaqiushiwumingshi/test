#最后一个单词的长度
#给定一串只由大小写字母和空格组成的句子，返回最后一个单词的长度
# A = "who are you"
# n = len(A) - 1
# print(len(A),(n))
# count = 0
# while n >= 0 and A[n] == ' ':
#     n -= 1
# while n >= 0 and A[n] != ' ':
#     count += 1
#     n -= 1
#     print(n)
# print(count)

x = 65648648432132131231231212131
y = int(str(x)[::-1])
print(y)