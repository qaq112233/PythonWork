"""
【实验50】计算中位数

编写一个程序，能够计算一个数值列表lst的中位数，要求如下：

1.列表lst元素可以自由输入，长度任意；

2.编写一个函数BSort，该函数可以对列表lst排序；

3.编写一个函数Median，该函数可以求得有序列表lst的中位数。
"""


def Bsort(a):
    b=[]
    a1 = a
    while a1 != []:
        b.append(min(a1))
        a1.remove(min(a1))
    return b


def Median(c):
    le = len(c)
    if le%2==0:
        e = (c[le//2-1]+c[le//2]) /2
        return e
    else:
        return (c[le//2])


lst=[]
print("请输入数字，输入为空则结束")
while True:
    i = input()
    if i == "":
        break
    else:
        lst.append(eval(i))

f=Bsort(lst)
print("排序后列表为",f)
print("中位数为",Median(f))

