a = input("输入带小数点的正数")
b = a.find(".")
c = len(a)
c = c - b-1
print("小数点左边", b, "位,小数点右边", c, "位")
