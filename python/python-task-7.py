num = range(2000, 3201)
div = set()
ndiv = set()
for i in num:
    if(i%7 == 0) and (i%5 == 0):
        div.add(i)
    else:
        ndiv.add(i)
print(div)