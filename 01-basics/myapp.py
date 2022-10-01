#GAMBA
import random
import time

def stop(c):
    s = input(f"Máš {c} coinů. Chceš pokračovat? (ano/ne): ")
    if s == "ano":
        return True
    else:
        return False

def gamba(coins):
        ran = 0
        ran = random.randrange(1, 3)
        if ran == 3:
            print("Vyhral jsi 5 coinu!")
            coins += 5
        elif ran == 2:
            print("Prohral jsi 3 coiny!")
            coins -= 3
        elif ran == 1:
            print("Vyhral jsi 1 coin!")
            coins += 1
        if coins < 0:
            print("Prohral jsi!")
            return coins
        return coins
#        wait = 2
#        while wait > 0:
#            time.sleep(1)
#            wait = wait - 1
coins = 5
while(coins > 0):
    s = stop(coins)
    if s == True:
        coins = gamba(coins)
    else:
        print(f"Bereš si domů {coins} coinů.")
        coins = 0
    if coins <= 0:
        print("Hra ukončena.")