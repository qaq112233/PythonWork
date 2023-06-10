"""

【实验49】函数的多样性

编写一个程序，该程序可以判定一个输入的正整数是否是素数，具体要求如下：

1.包含一个函数prime1，该函数无参无返回值，可以实现素数判定；

2.包含一个函数prime2，该函数带一个参数但无返回值，可以实现素数判定；

3.包含一个函数prime3，该函数带一个参数且有返回值，可以实现素数判定；

4.编写一个入口函数main。可以对以上三个函数进行调用、调试
"""

def prime3(a):
    if a == 2: return True
    
    for i in range(2,a//2):
        if a % i ==0:
            return False
    return True
    
def prime2(a):
    if prime3(a):
        print(a,"是素数")
    else:
        print(a,"不是素数")

def prime1():
    if prime3(input1):
        print(input1,"是素数")
    else:
        print(input1,"不是素数")

input1=int(input("输入数字"))
print()

prime1()
prime2(input1)
print(prime3(input1))
