n = int(input("人数："))
a = []
for i in range(n):
    a.append(int(input("成绩：")))
a.sort()

x = sum(a)/n
print("平均成绩：", x)

s1 = 0
for i in a:
    s1 = s1+(i-x)**2
s2 = s1/n
s = s2**0.5
print("标准差：", s)

print("最高分：", a[-1])
print("最低分：", a[0])
