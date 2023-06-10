'''
【实验34】二次方程
编写一段程序，计算二次方程ax2+bx+c=0(其中a不等于0)的实根。a、b、c由用户输入，在计算根之前，确保a是非0数。
注意：有根则输出具体的值，无根则输出无根即可
'''

a = (eval(input('a')))
b = (eval(input('b')))
c = (eval(input('c')))
if a != 0:
    d = (b ^ 2 - 4*a*c)
    if d >= 0:
        o1 = (-b+d**0.5)/(2*a)
        o2 = (-b-d**0.5)/(2*a)
        print(o1, o2)
    else:
        print('无根')
else:
    print('a不能为0')
