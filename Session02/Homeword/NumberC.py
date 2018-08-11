print("C. ")
print("\t \t i. 9 x 9 numbers (multiplication table)! ")
n = 9 
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(" \t ",i*j,end = "")
    print("")
print("")
print("\t \t ii. Ask user to enter a number n, then print n x n numbers, following multiplication table pattern: ")
n = int(input("\t ==>> Enter a number n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" \t ", i*j, end = "")
    print("")