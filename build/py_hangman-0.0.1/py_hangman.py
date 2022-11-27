#Imports
import urllib.request
import random

#Functions
def init_game(url):
    global to_guess
    global to_display
    raw_words=urllib.request.urlopen(url)
    words_list=raw_words.read().decode().splitlines()
    to_guess=random.choice(words_list)
    to_display="#"*len(to_guess)
    
#Constants
PICK_LIMIT=26

#Global Variables
to_guess=""
all_picks=[]
current_pick=""
wrong_picks=0

#Main Program
init_game("https://www.mit.edu/~ecprice/wordlist.10000")

while True:
    print("\nWord So Far: "+to_display)
    current_pick=input("Input Letter,"+str(PICK_LIMIT-wrong_picks)+" Picks Left: ").lower()[0]

    if current_pick not in all_picks:
        all_picks.append(current_pick)
    else:
        print("Invalid Letter")
        continue

    if current_pick in to_guess:
        print("Letter "+current_pick.upper()+" Is In The Word")
        for pos,letter in enumerate(to_guess):
            if letter in current_pick:
                to_display=to_display[:pos]+current_pick+to_display[pos+1:]
    else:
        wrong_picks+=1
        print("Letter "+current_pick.upper()+" Is Not In The Word")

    if to_display==to_guess:
        print("\nYou Win! Word Was "+to_guess.capitalize())
        break
    elif wrong_picks == PICK_LIMIT:
        print("\nYou Lose! Word Was "+to_guess.capitalize())
        break
