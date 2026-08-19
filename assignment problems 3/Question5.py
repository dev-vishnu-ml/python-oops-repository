'''
Quesetion 5-> assignment 3
'''

dictionary ={}
while True:
    choice = input("choose A|B|C|D|E : ").upper()
    if choice == 'A':
        message =input("enter key and value format(key:value):")
        key,val = message.split(":")
        dictionary[key]=int(val)
        print("added sucessfully !")
    elif choice == 'B':
        message = input("enter name and new marks (name:marks): ")
        key,val = message.split(":")
        if key in dictionary:
            dictionary[key] = int(val)
            print("student marks updated sucessfully")
        else:
            print("student not found")
    elif choice == 'C':
        message = input("enter name of student: ")
        if message in dictionary:
            print(key, "=",dictionary[key])
        else:
            print("student not found")
    elif choice == 'D':
        if dictionary:
            for key, val in dictionary.items():
                print(key, ":",val)
            else:
                print("dictionary is empty!")
        elif choice == 'E':
            print("program ended ")
            break
        else:
            print("wrong choice!")