seen = set()
duplicate = set()
list1 = [10,20,30,40,90,10,30]
for i in list1:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print(duplicate)