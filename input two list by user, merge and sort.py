list1 = input("enter the numbers of list:").split()
lst2 = input("enter number of 2nd list: ").split()
list1=list( map(int, list1))
lst2 = list(map(int, lst2))
 
combine_list = list1 + lst2
combine_list.sort()
print(combine_list)