import signal
import art
from os import system, name
import time

def leave(signum, frame):
    msg = "Est-que vous voulez quitter l'application? (y/n) "
    print(msg, end="", flush=True)
    ch = input("")
    if ch=='y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)
        print("    ", end="\r", flush=True)

signal.signal(signal.SIGINT, leave)

mot = "djjdjjdjjz"
print(art.text2art("___"))