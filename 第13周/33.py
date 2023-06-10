# 输入两个正整数m和n，使用辗转相除法求其最大公约数和最小公倍数。
# 提示：在循环中，用较大的数除以较小的数，然后将小的数作为下一轮循环较大的数，
# 再将其余数作为下一轮较小的数， 如此循环直到较小的数为0时，较大的数即为最大公约数

m = int(input('m'))
n = int(input('n'))
if m < n:  # m更大
    a = n
    n = m
    m = a
while True:
    b = m % n
    m = n
    n = b
    if n == 0:
        break
print(m)
