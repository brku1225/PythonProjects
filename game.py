import random

playerHealth = 100
monsterHealth = 100

while playerHealth > 0 and monsterHealth > 0:
    validChoice = False
    print(f"Player Health: {playerHealth}")
    print(f"Monster Health: {monsterHealth}", end = "\n")
    print("What would you like to do? (a/d)")
    while not validChoice:
        choice = str(input())
        if choice == "a":
            validChoice = True
        elif choice == "d":
            validChoice = True
        else:
            print("Please enter an 'a' or a 'd'")
    #0 is attack and 1 is defend
    monsterChoice = random.randrange(0, 2, 1)
    if choice == "a":
        if monsterChoice == 0:
            playerTake = random.randrange(0, 11, 1) + 10
            monsterTake = random.randrange(0, 11, 1) + 10
            print(f"\nPlayer takes {playerTake} damage")
            print(f"Monster takes {monsterTake} damage", end = "\n")
            playerHealth = playerHealth - playerTake
            monsterHealth = monsterHealth - monsterTake
        else:
            monsterTake = random.randrange(0, 7, 1)
            print(f"Monster takes {monsterTake} damage")
            print(f"Player takes {monsterTake} damage")
            monsterHealth = monsterHealth - monsterTake
    else:
        if monsterChoice == 0:
            playerTake = random.randrange(0, 10, 1)
            print(f"Player takes {playerTake} damage")
            print(f"Monster takes {playerTake} damage")
            playerHealth = playerHealth - playerTake
        else:
            print("Monster and Player take no damage")

if monsterHealth <= 0:
    print("\nCongrats you beat the monster")
elif playerHealth <= 0:
    print("\nWelp you died")