# input("\n\n按下 enter 键后退出。")
a = "赵 兄 托 我 办 点 事"
b = a.split(" ")
print(b)
b = b[-1::-1]
a = " ".join(b)
print(a)
print(b)