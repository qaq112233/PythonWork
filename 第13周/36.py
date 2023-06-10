"""
【实验36】相同生日
一个由r个人组成的小组，至少两个人生日 相同的概率为：

其中n是一年中 的天数。

编写一段程序，计算r从21至25的概率，一年按365天计算
"""


def p(r):
    n = 365
    a = 1
    for i in range(r):
        a *= (n - i) / n
    return 1 - a


for i in range(21, 26):
    print(i, p(i))
