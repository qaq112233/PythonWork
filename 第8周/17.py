a = eval(input('你的薪水'))
r = eval(input('薪水增长率'))
a1 = a*(1+r/100)/(1-r/100)
a2 = (a1-a)/a*100
print(a1, a2, '%')
