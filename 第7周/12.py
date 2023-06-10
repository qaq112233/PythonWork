a = eval(input("你的年龄："))
r = eval(input("你的休息心率："))
s = 7 * (220-a) / 10 + 0.3*r

print("你的年龄：",a)
print("你的休息心率：",r)
print("经计算，你的训练心率=",s,"次")