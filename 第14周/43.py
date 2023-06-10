a = []
for i in range(100, 200):
    a.append(i * (-1)**(i))
b = eval(input("请输入一个数："))

if b in a:
    c = a.index(b)
    print("在列表中，位置为：", c)
    a[0] = b
    a[c] = 100

else:
    print("不在列表中")


print(a)
