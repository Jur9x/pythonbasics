#GAMBA
import random
import time

def gamba():
    coins = 5
    print("Coins: ")
    print(coins)
    while(coins > 0):
        ran = 0
        ran = random.randrange(1, 3)
        if ran == 3:
            print("Vyhral jsi 5 coinu!")
            coins += 5
        if ran == 2:
            print("Prohral jsi 3 coiny!")
            coins -= 3
        if ran == 1:
            print("Vyhral jsi 1 coin!")
            coins += 1
        print("Coins: ")
        if coins < 0:
            print("0")
            print("Prohral jsi!")
            return
        else:
            print(coins)
        wait = 2
        while wait > 0:
            time.sleep(1)
            wait = wait - 1
gamba()