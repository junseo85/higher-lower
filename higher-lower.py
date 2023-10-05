from art import *
from game_data import data
import random
from replit import clear

print(logo)

random_int = random.randint(0, len(data) - 1)
new_random_int = random.randint(0, len(data) - 1)
a = data[random_int]
b = data[new_random_int]

score = 0
print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')

print(vs)
print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')


def check_count(a, b, score):
    game = True
    while game == True:
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if a["follower_count"] > b["follower_count"] and answer == 'a':
            score += 1

            a = b
            b = data[random.randint(0, len(data) - 1)]
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
            print(vs)
            print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
            


        elif b["follower_count"] > a["follower_count"] and answer == 'b':
            score += 1
            a = b

            a = b
            b = data[random.randint(0, len(data) - 1)]
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
            print(vs)
            print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
            


        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score:", score)
            game = False


check_count(a, b, score)
# from random import randint() to generate random number

# save as random number

# from game_data import data list and use random number to access random information
