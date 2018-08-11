# count = 0 
# loop = True 

# while loop :
#     print("running....")
#     count += 1
#     if count == 3:
#         break
#         # loop = False
#         print("Stop")

from random import randint
numb = randint(0,100)
count = 0 
print(numb)
while count != 7 :
    gness = int(input("Guess my number (1-100)? "))
    if gness > numb:
        print("Too larg ")
    elif gness < numb:
        print("A small:( ")
    else :
        print("Bingo")
        break
    count += 1        
print("You lose :( ")