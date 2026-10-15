num = range(2, 11)
divi = set()
ndiv = set()
for i in num:
    if(i%2 == 0):
        divi.add(i)
    else:
        ndiv.add(i)
print(divi)
