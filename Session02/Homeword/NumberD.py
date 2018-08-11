print("D. ")
print("\t \t i. 10 x 10 1’s and 0’s, consecutively! ")
n = 10
for i in range(n):
    if (i%2==0):
        for j in range(n):
            if(j%2==0):
                print(" 1 ", end = "")
            else:
                print(" 0 ", end = "")
        print("")
    else:
        for j in range(n):
            if(j%2 == 0):
                print(" 0 ", end = "")
            else:
                print(" 1 ", end = "")
        print("")
print("")
print("\t \t ii. Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively ")
n = int(input("\t ==>> Enter a number n : "))
for i in range(n):
    if (i%2==0):
        for j in range(n):
            if(j%2==0):
                print(" 1 ", end = "")
            else:
                print(" 0 ", end = "")
        print("")
    else:
        for j in range(n):
            if(j%2 == 0):
                print(" 0 ", end = "")
            else:
                print(" 1 ", end = "")
        print("")