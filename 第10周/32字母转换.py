a = input("输入字符串：")
b = []
for i in a:
    if i.islower():
        b.append(i.upper())
    elif i.isupper():
        b.append(i.lower())
    else:
        b.append(i)
print("".join(b))
