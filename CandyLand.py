from random import *
prize_list1 = ["candy", "cookies", "a three course meal"]
prize_list2 = ["money", "a car", "a house"]
position = [1]
# Landing on 13 sends you back 2 steps, landing on a 19 sends you back to tile 1


def play():
    play1 = input(">>>").title()

    if play1 == "Yes" or play1 == "Y":
        print("Alright, lettuce get this show on the road!")
        input("Press ENTER")

    elif play1 == "No" or play1 == "N":
        print("Lml, noob!XD")
        exit()

    else:
        print("Yes or No answers please.")
        play()


def roll_dice():
    return randint(1, 8)


def rules():
    print("""\t1. You will roll a dice to move about the board.
    2. You must get to spot 20 to win. If your position is equal to 0, you lose!
    3. If you roll a 1 or 3, you move back 1 step.
    4. If you roll a 5, you move back 2 steps.
    5. If you roll a 2 or 4, you move forward 1 step.
    6. If you roll a 6 or 8, you move forward 2 steps.
    7. If you roll a lucky 7, you get to roll again.""")


def candy_land():

    while position[0] <= 0:
        print("Game over!")
        print("You Lost!")
        print("Would you like to play again?")
        again = input(">>>").title()

        if again == "Yes" or again == "Y":
            print("Coolio.")
            position.clear()
            position.append(1)
            input("Press Enter")
            candy_land()

        else:
            print("How is your body feeling? I bet it's sore!")
            print("Sore loser!")
            exit()

    while position[0] == 13:
        print("You landed on tile 13")
        print("You have been moved back 2 spaces")
        position[0] -= 2
        print("Your position is now", position[0])
        input("Press Enter")
        candy_land()

    while position[0] == 19:
        print("Fuck!, you couldn't have been more unlucky")
        print("No way did you just land on tile 19")
        position.clear()
        position.append(1)
        print("You've just been moved to tile 1...")
        print("You have to start all over HAHA! Loser.")
        input("Press Enter")
        candy_land()

    while position[0] == 20:
        print(f"Congrats, LOSER.")
        print("You have reached the end.")
        print("You've put up a valiant fight and your luck has paid off")
        print("Now, it's time to take your prize")
        print("Pick a number between 1 and 8")
        pr = roll_dice()
        pick = int(input(">>>"))

        if pick < pr:
            print("Okay, your prizes are:")
            print(prize_list1[0], "\b,", prize_list1[1], "\b, and", prize_list1[2])
            print("Have fun with those great prizes.")
            print("Would you like to play again?")
            again = input(">>>").title()

            if again == "Yes" or again == "Y":
                print("Copy, let's do it again!")
                position.clear()
                position.append(1)
                input("Press Enter")
                candy_land()

            else:
                print("Wow, what a loser!")
                print("Why would you not want to play again after losing?")
                print("I thought you had a gambling addiction!")
                exit()

        elif pick > pr:
            print("Okay your prizes are:")
            print(prize_list2[0], "\b,", prize_list2[1], "\b, and", prize_list2[2])
            print("Have fun with those great prizes.")
            print("Would you like to play again?")
            again = input(">>>").title()

            if again == "Yes" or again == "Y":
                print("Copy, let's do it again!")
                position.clear()
                position.append(1)
                input("Press Enter")
                candy_land()

            else:
                print("Wow, what a loser!")
                print("Why would you not want to play again after losing?")
                print("I thought you had a gambling addiction!")
                exit()

        else:
            print("Lucky you. You get two both prize lists.")
            print("Both :", prize_list2[0], "\b,", prize_list2[1], "\b,", prize_list2[2], "\b,", prize_list1[0], "\b,", prize_list1[1], "\b, and", prize_list1[2], "!!!")
            print("Have fun with those awesome prizes.")
            print("Would you like to play again?")
            again = input(">>>").title()

            if again == "Yes" or again == "Y":
                print("Copy, let's do it again!")
                position.clear()
                position.append(1)
                input("Press Enter")
                candy_land()

            else:
                print("""
                Wow, what a loser!
                Why would you not want to play again after losing?
                I thought you had a gambling addiction!
                """)
                exit()

    roll = roll_dice()
    print(f"You rolled a {roll}")

    if roll == 1 or roll == 3:
        print("You have been moved back one space.")
        position[0] -= 1
        print("Your position is now", position[0])
        input("Press Enter to continue")
        candy_land()

    elif roll == 5:
        print("You have been moved back two spaces.")
        position[0] -= 2
        print("Your position is now tile", position[0])
        input("Press Enter to continue")
        candy_land()

    elif roll == 2 or roll == 4:
        print("You have been moved forward one space.")
        position[0] += 1
        print("Your position is now tile", position[0])
        input("Press Enter")
        candy_land()

    elif roll == 6 or roll == 8:
        print("You have been moved forward two spaces!!!!")
        position[0] += 2
        print("Your position is now tile", position[0])
        input("Press Enter")
        candy_land()

    elif roll == 7:
        print("Ayyy, lucky 7!")
        print("You get to roll again!")
        input("Press ENTER to roll again.")
        candy_land()


print("Hello user, what is your name?")
name = input(">>>").title()
print(f"Ahh, nice to meet you {name}.")
print(f"My name is also {name} and I like to steal people's identities")
print(f"I think instead of {name}, I'm gonna call you 'LOSER'.")
print("Would you like to play a game? *Yes or No*")
play()
print(f"""This game is called Candy Land.
Let me explain the rules to you, LOSER.""")
input("Press ENTER to see da rools")
rules()
input("Press Enter when you have read the rules to move on")
print("\n")
print("So basically, you're not doing Ecstasy, but you will be rolling a lot.")
input("Press ENTER to begin!")
candy_land()
