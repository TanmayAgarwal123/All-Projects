from random import *

# taking input from user
user_pass = input("Enter your password ")
# storing numbers to use thm to crack password
password = ['0','1','2','3','4','5','6','7','8','9']
# initializing an empty string
guess = ""
i=0
# using while loop to generate many passwords untill one of
# them does not matches user_pass
while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_number = password[randint(0, 9)]
        guess = str(guess_number) + str(guess)
    i=i+1    
    # printing guessed passwords
    print(guess)

print("Your password is ",guess)
print("it took ",i," guesses to find your password")