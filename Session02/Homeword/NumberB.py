print("b. ")
print("\t \t i. 1’s and 0’s, consecutively ! ")
for i in range(1,9):
    if i%2==0:
        print("0 ", end = "")
    else:
        print("1 ", end = "")
print("")
print("\t \t ii. Ask users to enter a number n, then print n 1’s and 0’s in total consecutively ")
n = int(input("\t ==>> Enter the total number of 1's and 0's : "))
for i in range(1,n+1):
    if i%2==0:
        print("0 " , end = "")
    else:
        print("1 ", end = "")