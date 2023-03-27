t = input("输入：")
if t[-1] in ["f","F"]:
    C = (eval (t[0:-1])-32)/1.8
    print ("zhuanhuan{:.2f}C".format(C))
elif t[-1] in ["C","c"]:
    F = 1.8 * eval (t[0:-1]) + 32
    print ("zhuanhuan{:.2f}F".format(F))
else:
    print("error")
