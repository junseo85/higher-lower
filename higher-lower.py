from art import *
from game_data import data
import random
from replit import clear
#Display art
print(logo)
#generate random account
random_int = random.randint(0, len(data) - 1)
new_random_int = random.randint(0, len(data) - 1)
a = data[random_int]
b = data[new_random_int]

score = 0
#Format the account data into printable format.
print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
#Display art
print(vs)
print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')


def check_count(a, b, score):
    game = True
    while game == True:
        #Ask user for a guess.
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        #check if user is correct
        if a["follower_count"] > b["follower_count"] and answer == 'a':
            #score keeping
            score += 1
            #Making account at position B become the next account at position A
            a = b
            #generate new account and save to B
            b = data[random.randint(0, len(data) - 1)]
            #clear the screen
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
            print(vs)
            print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
            #print(a["follower_count"], b["follower_count"])


        elif b["follower_count"] > a["follower_count"] and answer == 'b':
            score += 1
            a = b
            b = data[random.randint(0, len(data) - 1)]
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
            print(vs)
            print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
            #print(a["follower_count"], b["follower_count"])


        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score:", score)
            game = False


check_count(a, b, score)
