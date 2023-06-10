def jiechen(ad):
    for i in range(1, ad):
        ad = ad * i
    return ad


i = 1
an = 0
while i < 6:
    an = an+jiechen(i)
    i = i+1

print(an)

bn = 0
for i in range(1, 6):
    bn = bn+jiechen(i)
print(bn)
