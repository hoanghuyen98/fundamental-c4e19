# # from random import randint
# # numb = randint(0,100)
# # print(numb)
# from random import randint

# numb = randint(0,100)
# if numb < 30 :
#     print(" :< ")
# elif numb < 60 :
#     print(" +__+ ")
# else :
#     print(" ^__^ ")
n = 10
for i in range(n):

    for j in range(n):
        if j < n - i - 1:
            print("  ", end = "")
        else:
            print("* ", end = "")
    print("")
        
# for i in range(7):
#     for j in range(7):
#         pr
        

    