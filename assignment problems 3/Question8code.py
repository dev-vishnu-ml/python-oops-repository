# assignment 3 question number-> 8 check the common elments or not using intersection method of set
list1 = [1,2,3,4]
list2 =[5,6,7,8,9]
set1 = set(list1)
set2 = set(list2)
common = set1 .intersection(set2)
if common:
    print(f"share common elements: {common}")
else:
    print("share no common elements")