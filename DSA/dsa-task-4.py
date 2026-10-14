Student_id = [1, 2, 3, 5, 6, 8, 3, 5, 9]
dup = set()
ids = set()
for i in Student_id:
    if i in ids:
            dup.add(i)
    else:
            ids.add(i)
if(dup == set()):
       print("The array has no duplicates")
else:
       print("The array has duplicates")