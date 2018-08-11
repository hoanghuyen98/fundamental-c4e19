
numb = int(input("Enter a number : "))
savenumber = numb
count = 0
while numb > 0 :
    numb = numb//10 
    count += 1
print("{0} has {1} digit(s)".format(savenumber, count))
    
   

