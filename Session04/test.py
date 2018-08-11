numb = int(input("Enter a bumber : "))
if numb < 2 :
    print("{0} is not a prime number ".format(numb)) 
elif numb == 2:
    print("{0} is a prime number ".format(numb))
elif numb % 2 == 0:
    print("{0} is not a prime number ".format(numb))
else:
    for i in range(2,numb,1):
        if numb % 3 == 0:
            print("{0} is not  prime number ".format(numb))
            break
        else :
            print("{0} is prime number ".format(numb))
            break