Student_id = [1, 2, 3, 5, 6, 8, 3, 5, 9]
dup = set()
ids = set()
def duplicates(Student_id):
    for i in Student_id:
        if i in ids:
            dup.add(i)
        else:
            ids.add(i)
    print(f"{dup} are the duplicates")
duplicates(Student_id)