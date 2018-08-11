matrix = int(input("Enter size of the matrix: "))
n = matrix

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1:
            print("* ",end = "")
        else:
            print("  ", end = "")
    print(end = " " *5)
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n :
            print("* ",end = "" )
        else:
            print("  ", end = "")
    print(end = " " * 5)
    print("* ",end ="")
    for j in range(2,(int)(2*(n+1)/3+1)):       
        if i == 1 or i == (n+1)-1 :
            print("* ",end = "")
        else:
            print("  ",end = "")
            if j==(int)(2*(n+1)/3):
                print("* ",end="")
    print(end = " " * 5)
    if i == 1 or i == n:
        print("  ", end = "")
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or i == (int) ((n+1)/2) :
            print("* ",end = "" )
        else:
            print("  " , end = "")
    print("")




        

        

#              1 2 3 4
# * * * * 1    * * * *     * * * *   *
# *       2    *     *     *     *   
# *       3    *     *     *     *
# * * * * 4    * * * *     * * * *