import time
import random

places = ["an open field", "a dense forest", "a desert"]
ennemies = ["the mad king", "the queen of the elves", "the dark wizard"]
items = []


def print_pause(message, lag):
    print(message)
    time.sleep(lag)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            break
    return response


def game_over():
    print_pause("\nGAME OVER", 2)
    response = valid_input("\nWould you like to play again? (y/n): ",
                           ["y", "n"])
    if response == "y":
        play_game()
    elif response == "n":
        print_pause("\nThank you for playing!\n", 1)


def intro(place, ennemy):
    print_pause(f"\nYou wake up in {place}.", 2)
    print_pause("You look around and find your best friend checking "
                "a map.", 2)
    print_pause("Your friend explains that you are on your way to defeat"
                f" {ennemy},", 2)
    print_pause("who took your dog away...", 2)
    print_pause(":(", 1)
    print_pause(f"You need to find {ennemy} before sunset or your dog "
                "will be sacrified.\n", 2)


def first_choice(ennemy):
    print_pause("What would you like to do?", 1)
    print_pause("1. Go north.\n"
                "2. Go east.\n"
                "3. Go west.\n"
                "4. Ask your friend's opinion", 0)

    response = int(valid_input("Please enter 1, 2, 3 or 4: ",
                               ["1", "2", "3", "4"]))
    if response == 1:
        go_north(ennemy)
    elif response == 2:
        go_east(ennemy)
    elif response == 3:
        go_west(ennemy)
    elif response == 4:
        if "shining sword" in items:
            print_pause("\nYour friend suggests you go west.\n", 1)
        else:
            print_pause("\nYour friend suggests you go east.\n", 1)
        first_choice(ennemy)


def second_choice(ennemy):
    print_pause("What would you like to do?", 1)
    print_pause("1. Sigh and listen to the kid.\n"
                "2. Ignore the kid and go back.\n"
                "3. Ask you friend's opinion.", 1)
    response = int(valid_input("Please enter 1, 2 or 3: ", ["1", "2", "3"]))
    if response == 1:
        print_pause(f"\nThe kid explains that {ennemy} threatened "
                    "the villagers.", 2)
        print_pause("As an apology, he gives you a shining sword to "
                    "help you on your quest.", 2)
        items.append("shining sword")
        print_pause("You leave the village with your new weapon and "
                    "return to your original location.\n", 2)
        first_choice(ennemy)
    elif response == 2:
        print_pause("\nThey wasted enough of your time already.", 2)
        print_pause("You leave the village and return to your original "
                    "location.\n", 2)
        first_choice(ennemy)
    elif response == 3:
        print_pause("\nYour friend suggests you listen to the kid.", 2)
        print_pause("'Who knows what he could want to say?'\n", 2)
        second_choice(ennemy)


def third_choice(ennemy):
    print_pause("What would you like to do?", 1)
    print_pause("1. Rush in to save your dog!\n"
                "2. Go back.\n"
                "3. Ask your friend's opinion.", 0)
    response = int(valid_input("Please enter 1, 2 or 3: ", ["1", "2", "3"]))
    if response == 1:
        print_pause(f"\nYou rush in and find {ennemy} just in time.", 2)
        if "shining sword" in items:
            print_pause(f"You pull out your brand new shining sword...", 0)
            print_pause(f"...and slay {ennemy}!", 2)
            print_pause("Meanwhile your friend opened the cage in which"
                        " your dog was emprisoned.", 2)
            print_pause("You happily walk out of the castle with your dog "
                        "and your best friend.", 2)
            print_pause("\nHappy ending :) Congratulations!\n", 2)
        else:
            print_pause("Unfortunately, you arrived empty-handed...", 2)
            print_pause(f"... and {ennemy} is too strong for you.", 2)
            print_pause(f"You are defeated, and you can hear {ennemy} "
                        "laughs \nas your dog is sacrified...", 2)
            print_pause("Maybe get a weapon before rushing to the boss "
                        "battle next time.", 2)
            game_over()
    elif response == 2:
        print_pause("\nYou fear you might have missed something "
                    "and walk back to your original location.\n", 2)
        first_choice(ennemy)
    elif response == 3:
        if "shining sword" in items:
            print_pause("\nYour friend is already at the castle door "
                        "waiting for you.", 2)
            print_pause("'What are you waiting for?! Hurry up!'\n", 2)
            third_choice(ennemy)
        else:
            print_pause("\nYour friend seems a bit hesitant.", 2)
            print_pause("'Don't you feel like we are a bit underequipped"
                        "?'\n", 2)
            third_choice(ennemy)


def go_north(ennemy):
    print_pause("\nYou go north, walk for hours but you find nothing...", 2)
    print_pause("Your friend suggests to go back.\n", 2)
    print_pause("What would you like to do?", 1)
    print_pause("1. Keep walking.\n"
                "2. Go back.", 0)
    response = int(valid_input("Please enter 1 or 2: ", ["1", "2"]))
    if response == 1:
        print_pause("\nYou stubbornly keep walking for hours until "
                    "night fall.", 2)
        print_pause("It is now too late for your dog...", 2)
        print_pause("Poor doggy :(", 2)
        print_pause("Maybe you should listen to your friend next time.", 2)
        game_over()
    elif response == 2:
        print_pause("\nYou walk back to where you started.\n", 2)
        first_choice(ennemy)


def go_east(ennemy):
    print_pause("\nYou arrive to a quiet village.", 2)
    if "shining sword" in items:
        print_pause("The small kid who gave you the shining sword "
                    "earlier approaches you.", 2)
        print_pause("'You need to hurry up if you want to save your dog'"
                    ", he says.", 2)
        print_pause("You return to your original location.\n", 2)
        first_choice(ennemy)
    else:
        print_pause(f"You ask for information on {ennemy} and try to "
                    "buy supplies,", 2)
        print_pause("but everyone seems to avoid you and refuses to "
                    "talk to you.", 2)
        print_pause("As you are about to leave the village, furious at the "
                    "villagers attitude,", 2)
        print_pause("a small kid approaches you.\n", 2)
        second_choice(ennemy)


def go_west(ennemy):
    print_pause("\nYou arrive to a big castle with an evil atmosphere.", 2)
    print_pause(f"It is very likely to be the castle of {ennemy}.", 2)
    print_pause("As you get closer, you can hear your dog barking!\n", 2)
    third_choice(ennemy)


def play_game():
    place = random.choice(places)
    ennemy = random.choice(ennemies)
    intro(place, ennemy)
    first_choice(ennemy)


play_game()
