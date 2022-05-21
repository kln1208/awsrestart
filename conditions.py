'''
userreply= input("do you want to ship a packet? (reply Yes or No)")
if userreply == "Yes":
    print("yes i want to ship")
else:
    print("NO, i will ship myself.")
   


userreply = int(input("please enter your age"))

if userreply < 18 :
    print("you are a child")
elif userreply >18 :
    print("you are young")

else:
    print("you are a senior citizen")
    



userReply = input ("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) \n")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))





print("Count to 10!")

for x in range (0, 20):
    print(x)

'''

    
    

