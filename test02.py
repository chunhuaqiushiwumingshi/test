# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[8008208820]     = "2 - 菜鸟工具"
# print(dict)
# print(dict.keys(),dict.values())

# a = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(a)
# a = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# b = [c  for c in a if len(c)>4]
# print(b)
b = {1,2,3,4,5}
a = {x:x**x for x in b}
print(a[5])