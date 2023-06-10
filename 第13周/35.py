# 【实验35】特殊数字
# 编写一段程序，找到一个4位数，用abcd表示。它的4倍正好是它数字的逆序，即4 x abcd = dcba。

a1 = []
for i in range(1000, 10000):
    a1.append(str(i))
for i in a1:
    if int(i)*4 == int(i[::-1]):
        print(i)
        break
