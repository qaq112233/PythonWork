"""
【实验44】斐波那契数列

使用列表生成一个斐波那契数列的前20项并输出，输出时要求每行4个数列项，共5行。
"""

a=[]
a.append(1)
a.append(1)
for i in range(2,20):
    a.append(a[i-1]+a[i-2])

a1=0
for i in a:
    print(i,end=" ")
    a1 = a1 +1
    if a1 %4 == 0:
        print("")
