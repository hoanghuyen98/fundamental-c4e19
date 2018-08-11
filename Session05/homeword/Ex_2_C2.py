enter_list = input("Enter a list number : ")
lists = enter_list.split()
numbers = [int(x) for x in lists]
loop = True
while loop :

    print(numbers)

    numb = int(input(" Enter a number: "))

    count = numbers.count(numb) # sử dùng hàm count() đém số lần xuất hiện
    print(count)
    print("{0} appears {1} times in my list".format(numb, count))

    print("* "*20)
    
    quite = input("Do you want to continue the program(Y/N)? ").upper()

    if quite == 'N':
        loop = False
        
    print("* "*20)