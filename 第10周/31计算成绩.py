

a = []
while True:
    flag = input("是否输入，若回答yes则继续输入，若回答no则停止输入")
    if flag == "yes":
        while True:
            c = eval(input("请输入成绩："))
            if c < 0 or c > 100:
                print("输入错误,请重新输入")
            else:
                a.append(c)
                break
    elif flag == "no":
        break

geshu = len(a)
zongfen = 0
for i in a:
    zongfen = zongfen + i
pingjunfen = zongfen/geshu
zuigao = max(a)

print("共输入了", geshu, "个成绩", "总成绩为", zongfen,
      "平均分为", pingjunfen, "最高分为", zuigao)
