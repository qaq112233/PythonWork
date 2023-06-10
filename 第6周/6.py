SPY = eval(input("SPY投资额度"))
QQQ = eval(input("QQQ投资额度"))
EEM = eval(input("EEM投资额度"))
VXX = eval(input("VXX投资额度"))

sum =SPY + QQQ + EEM + VXX
print("四个基金 的总投资额是：{:.2f}元".format(sum))
print("其中：")
print("SPY:{:.2%}".format(SPY / sum))
print("QQQ:{:.2%}".format(QQQ / sum))
print("EEM:{:.2%}".format(EEM / sum))
print("VXX:{:.2%}".format(VXX / sum))