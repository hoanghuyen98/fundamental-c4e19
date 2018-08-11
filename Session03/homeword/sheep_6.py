print("2.6: Calculate the total size of your sheep as well as the money you would have")
size = [5 ,7, 300, 90, 24, 50, 75]
print(" Hello, my name is Huyen and here is my flock ")
print(" \t ", size)
month = int(input(" Enter the number of months: "))
for i in range(month):
    size_max = max(size)
    index = size.index(size_max)
    size[index] = 8
    print(" Now my biggest sheep has size {0} let's shear it. After shearing, here is my flock".format(size_max))
    print(" \t ", size)
    print()
    print("=====================================================================================")
    print("Month {0} ".format(i+1))
    temp = 0 
    if i < month :
        print("One month has passed, now here is my flock ")
        for item in size:
            item += 50
            size[temp] = item
            temp += 1
        print(" \t ", size)
        if i == month - 1:
            sum_size = sum(size)
            print()
            print(" My flock has size in total: ", sum_size)
            print(" =====>> I would get {0} * 2$ = {1} $".format(sum_size,sum_size*2))

       
    
