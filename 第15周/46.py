"""
【实验46】矩阵的计算

生成一个3*4的矩阵，并能够计算该矩阵中最接近平均值的元素是哪个，编写代码实现该功能，具体要求如下：

1.矩阵使用二维列表表示；

2.矩阵数据可以输入；

3.要求输出平均值、最接近平均值的数据项以及该项位于哪行哪列。
"""

a1=[]
a2=[]
a3=[]

a=[a1,a2,a3]

for i in range(4):
    print("输入第1行第",i+1,"个")
    a1.append(eval(input()))
for i in range(4):
    print("输入第2行第",i+1,"个")
    a2.append(eval(input()))
for i in range(4):
    print("输入第3行第",i+1,"个")
    a3.append(eval(input()))
print(a)
avg=0
for i in a:
    for b in i:
        avg=avg+b
avg = avg / 12
print("平均值",avg)

c=abs(a[0][0] - avg)

hangshu=0
lieshu=0
shuju=a[0][0]
for i in a:
    hangshu+=1
    for b in i:
        lieshu+=1
        ad = abs(b-avg)
        if ad < c:
            c =ad
            shuju = b
            e=hangshu
            f=lieshu

f= f%4
print(shuju,"第",e,"行","第",f,"列")
