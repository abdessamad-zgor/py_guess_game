import art
import random
import signal
import sys
from typing import List
from os import system, name, path


def leave(signum, frame):
    msg = "\nEst-que vous voulez quitter l'application? (y/n) :"
    print(msg, end="")
    ch = input()
    if ch=='y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)
        print("    ", end="\r", flush=True)

signal.signal(signal.SIGINT, leave)

def lire_mots()->List[str]:
    with open(path.dirname(__file__)+"/motquiz.txt") as f:
        mots = [l.strip() for l in f.readlines()]
    return mots

def render(ch:str, mot:str, oldguess:str, attempts: int, win:bool):
    if(ch==""):
        return (oldguess, attempts, False)
    if(attempts!=0):
        if ch in mot:
            new= list(oldguess)
            new[mot.index(ch)]=ch
            new_guess = "".join(new)
            if new_guess == mot:
                return (new_guess, attempts, True)        
            
            return (new_guess, attempts, False)
        else:
            
            return (oldguess, attempts-1, False)
    else:
        return ("Game Over", -1, False)

def clear():
    system('clear' if name!="nt" else "cls")

def game_loop():
    args = sys.argv
    mot = random.choice(lire_mots())
    guess = "_"*len(mot)

    choix=""
    attempts = 6
    win = False
    while True:
        clear()
        (guess, attempts, win)=render(choix, mot, guess, attempts, win)
        if attempts==-1:
            print(art.text2art(guess))
            ch = input("voulez vous rejouir (y/n): ")
            if ch=='y':
                game_loop()
            else:
                exit(0)
        if args.count("--cheat")==1:
            print(mot)
        if win:
            print(art.text2art("Brovoo!"))
            



        print(f"\t\t\t\t\t\t\t\t\t\t\t\t il vous reste {attempts} essais")
        print(art.text2art(guess))
        print("Entrez un character : ", end="")
        choix= input()
    

def main():
    game_loop()

main()

    
        