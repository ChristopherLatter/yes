"""Chris"""
name = input("what name boy? ")
while name == "":
    name = input("what name boy? ")
else:
    print(name[::2])