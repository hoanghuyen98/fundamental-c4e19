enter_list = input("Enter a list number : ")
lists = enter_list.split()
numbers = [int(x) for x in lists]

# numbers = [ 1, 6, 8 , 1 , 2 , 1 ,5 , 6]

numbers.sort() # sắp xếp lại list 

loop = True
while loop:

    print(numbers)

    numb = int(input(" Enter the number: "))

    counts = 0 # sử dụng biến đếm

    for item in numbers:
        if item == numb:
            counts += 1     

    print("=======>> {0} appears {1} times in my list".format(numb, counts))
    print("* "*20)
    
    quite = input("Do you want to continue the program(Y/N)? ").upper()

    if quite == 'N':
        loop = False

    print("* "*20)