shop = ['T-shirt', 'áo len']
loop = True
while loop :
    print()
    choose = input("Welcome to our shop. What do you want (C, R, U, D)? ")
    print()
    if choose == 'R'or choose == 'r':
        print("Our item ==> ",end = "")
        print(*shop, sep = ", ")
    
    if choose == 'C' or choose == 'c' :
        new_clothes = input("Enter new item: ")
        shop.append(new_clothes)
        print("Our item ==> ",end = "")
        print(*shop, sep = ", ")

    if choose == 'U' or choose == 'u':
        while len(shop) > 0:
            up_position = int(input("Update position: "))
            if up_position > len(shop) or up_position<0 :
                print(" Invalid Position ")
            else :
                new_clothes = input("=====>>>>   Enter new item: ")
                shop[up_position-1] = new_clothes
                print("Our item ==> ",end = "")
                print(*shop, sep = ", ")
                break 

    if choose == 'D' or choose == 'd':
        while len(shop) > 0:
            del_position = int(input("Delete position: "))
            if del_position < 0 or del_position > len(shop):
                print(" Invalid Position !! ")
            else :
                shop.pop(del_position-1)
                print("Our item ==> ",end = "")
                print(*shop, sep = ", ")
                break
    print("=====================================")            
    print("")
    print(" !! Type ''exit'' to quit :(( ")
    print("=====================================")   
    if choose == 'exit' or choose == 'Exit' or choose == 'EXIT':
        print(" See you again !! ")
        break