string = input("enter  string for count spaces: ")
space_count = 0
for i in string:
    if i == " ":
        space_count += 1

print(f"total spaces of :{space_count}")