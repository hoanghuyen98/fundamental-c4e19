from random import choice
word = ("champion")
chars  = list(word)
new_list = []
loop = True
while loop:
    rand_char = choice(chars)
    new_list.append(rand_char)
    chars.remove(rand_char)
    if len(chars) == 0:
        loop = False
print(*new_list)
ans = input("Your guess: ")
if ans == word:
    print("Correct")
else:
    print("lose :(")
# rand_char = choice(chars)
# correct = word  
# jumble = ""
# points = 100
# while word :
#     position = random.randrange(len(word))
#     jumble += word[position]
#     word = word[:position] + word[(position + 1):]
# print("The jumble is ", jumble)
# answer = input(" Your answer: ")
# while answer != correct and answer != "":
#     print("Sorry, that's not it.")
# # if correct=="champion":
# #         print("Its a snake...")
# if answer == correct:
#     print("That's it!  You guessed it!\n")
#     print("Your score is: "+str(points))
# elif answer== "":
#     print("You failed...")