numb = int(input("Enter a bumber : "))
is_prime = True
i = 2
while i <= (numb ** 0.5):
    if numb  % i == 0:
        is_prime = False
        break
    i += 1
if is_prime == True:
    print("{0} is a prime number ".format(numb))
else :
    print("{0} is not a prime number ".format(numb))
#numb = int(input("Enter a bumber : "))
# if numb < 2 :
#     print("{0} is not a prime number ".format(numb)) 
# elif numb == 2:
#     print("{0} is a prime number ".format(numb))
# elif numb % 2 == 0:
#     print("{0} is not a prime number ".format(numb))
# else:
#     for i in range(2,numb,1):
#         if numb % 3 == 0:
#             print("{0} is not  prime number ".format(numb))
#             break
#         else :
#             print("{0} is prime number ".format(numb))
#             break
