print("2.1 : Create a list to represent the sizes of your flock, using list, and print all of your flock size, expected screen output: ")
sizes = [5, 7, 300, 90, 24, 50, 75]
print()
print(" =====>> Hello, my name is Huyen and there are my sheep sizes")
print(" \t ",sizes)
print()

print("2.2 : search for the biggest sheep !! " )
sizes_max = sizes[0]
for item in sizes :
    if item > sizes_max:
        sizes_max = item
print()
print("=====>> Now my biggest sheep has size {0} let's shear it".format(sizes_max))
print()

print("2.3 : Print out your ship size after shearing the biggest one " )
print()
index = sizes.index(sizes_max)
sizes[index] = 8 
print("=====>> After shearing, here is my flock !")
print()
print("\t",sizes)
print()

print("2.4 : In the following month, EVERY sheep in your flock grow, they have their size increased by 50 " )
print()
# sheep_grow = int(input("Enter their size increased: "))
temp = 0
for item in sizes:
    item = item + 50
    sizes[temp] = item
    temp += 1
print(" One month has passed, now here is my flock ")
print(" \t ", sizes)
print()




