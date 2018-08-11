low = 0 
high = 100
loop = True
print(" Now think of a number from 0 to 100, then press 'Enter'")
input()
print("""
All you have to do is to answer to my guess
'c' if my answer is 'C' orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")
while loop :
    mid = (low +  high) // 2
    numb = input("Is {0} your number? ".format(mid)).lower() # lower()
    if numb == 'c' :
        print(" I knew it ")
        loop = False
    elif numb == 's':
        low = mid 
    elif numb == 'l':
        high = mid

    
