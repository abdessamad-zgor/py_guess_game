import random
import sys
from os import system, name, path
import art


def lire_mots():
    with open(path.dirname(__file__)+"/motquiz.txt") as f:
        mots = [l.strip() for l in f.readlines() if l!=""]
    return mots


def update_guess(ch: str, oldguess: str, mot: str):
    if ch in mot and oldguess.count(ch) != mot.count(ch):
        new = list(oldguess)
        # trouver la derniere occurance du letter dans la chaine courant
        try:
            last_occur = oldguess.rindex(ch)
            
        except ValueError:
            last_occur = -1
        new[mot.index(ch, 0 if last_occur==-1 else last_occur+1)] = ch
        new_guess = "".join(new)
        return new_guess
    else:
        return oldguess


def render(ch: str, mot: str, oldguess: str, attempts: int, win: bool):
    if (ch == ""):
        return (oldguess, attempts, False)
    if (attempts != 0):
        newguess = update_guess(ch, oldguess, mot)
        if newguess == mot:
            return (newguess, attempts, True)
        elif newguess!= oldguess :
            return (newguess, attempts, False)
        else:
            return (oldguess, attempts-1, False)
    else:
        return ("Game Over", -1, False)


def clear():
    system('clear' if name != "nt" else "cls")


def game_loop():
    try:
        args = sys.argv
        mot = random.choice(lire_mots())
        guess = "_"*len(mot)
        choix = ""
        attempts = 6
        win = False
        while True:
            clear()
            (guess, attempts, win) = render(choix, mot, guess, attempts, win)
            if attempts == -1:
                print(art.text2art(guess))
                ch = input("voulez vous rejouir (y/n): ")
                if ch == 'y':
                    game_loop()
                else:
                    clear()
                    print(art.text2art("goodbye"))
                    exit(0)
            if args.count("--cheat") == 1:
                print(mot)
            if win ==True:
                print(art.text2art("Brovoo!"))
                print("vous avez deviner le mot   "+mot.upper())
                ch = input("voulez vous rejouir (y/n): ")
                if ch == 'y':
                    game_loop()
                else:
                    clear()
                    print(art.text2art("goodbye"))
                    exit(0)

            print(f"\t\t\t\t\t\t\t\t\t il vous reste {attempts} essais")
            print(art.text2art(guess))
            print("Entrez un character : ", end="")
            while True:
                choix = input()
                if len(choix)!=1:
                    print("Entrez une seul character : ", end="")
                else:
                    break;
    except KeyboardInterrupt:
        print()
        ch = input("Voulez vous quitez l'application (y/n) : ")
        if ch=='y':
            clear()
            print(art.text2art("goodbye"))
            exit(0)
        else:
            game_loop()


def main():
    game_loop()


main()
