i = 1
z = 0

while i < 100:
    a = i*i
    if i % 2 == 0:
        a = -1*a
    z = z + a
    i = i+1

print(z)
