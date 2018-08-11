
inventory = {
    'gold' : 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
 # Add a Key to inventory called 'pocket' and Set the value of 'pocket' to be a list  

print("1: Add a Key to inventory called 'pocket' and Set the value of 'pocket' to be a list ")
print()
print(" =====>> List ban đầu : ")
print(inventory)
inventory['pocket'] = ['seashell', 'strange', 'berry', 'lint']
print(" =====>> List sau khi thêm : ")
print(inventory)
print()
print("* "*20)
 # Then remove('dagger') from the list of items stored under the 'backpack' key
print("2: Then remove('dagger') from the list of items stored under the 'backpack' key")

print()
key = "backpack"
if key in inventory:
    value = inventory[key]
    value.pop(1)
    print(" =====>> List sau khi xóa value dagger của key 'backpack ")
    print()
    print(inventory)
else:
    print(" not found ")
print()
print("* "*20)

 # Add 50 to the number stored under the 'gold' key.

print("3: Add 50 to the number stored under the 'gold' key.")
print()
key_1 = 'gold'
if key_1 in inventory:
    inventory[key_1] += 50
    print(" =====>> List sau khi thêm 50 vào 500 ")
    print()
    print(inventory)
    print()
else:
    inventory[key_1] = 50
    print(inventory)


