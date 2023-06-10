a = []
a.append(eval(input("老师1的分数：")))
a.append(eval(input("老师2的分数：")))

if abs(a[0] - a[1]) <= 4:
    grade = (a[0] + a[1])/2
else:
    a.append(eval(input("老师3的分数：")))
    a.sort()
    z1 = abs(a[0]-a[1])
    z2 = abs(a[1]-a[2])

    if z1 == z2:                  # 两个老师的分数差相等
        grade = (a[1]+a[2])/2
    elif z1 <= 4 or z2 <= 4:      # 两个老师的分数差不相等，但是有一个老师的分数差小于等于4
        if z1 > z2:
            grade = (a[1]+a[2])/2
        else:
            grade = (a[0]+a[1])/2
    else:
        print("阅卷存在分歧，该生试题进入评判组")
        grade = "存在分歧"


print("老师打的分数为：")
for i in a:
    print(i, end=" ")
print("")
print("该生的成绩为：", grade)
