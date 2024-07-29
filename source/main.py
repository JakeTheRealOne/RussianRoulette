"""
Author: Bilal Vandenberge
Date: July 2024
-> Run the russian roulette game
"""

import random
import os
import time

import loading_screen

def CONTRACT(edition: str) -> str:
    return (
      f"Welcome in a basic game of Russian Roulette - {edition} edition"
      "\nBefore we start, You must sign a contract"
      " rules:\n--- CONTRACT ---\n1.  If you lose, you risk having your system erased.\n"
      "2.  That's it."
    )



def print_human(sample: str) -> None:
    """
    display in the terminal in an "human" way a text
    """
    for chr in sample:
        print(chr, end="", flush=True)
        time.sleep(0.02)


def random_surviving_text():
    """
    return a random text after the user survived
    """
    scenario = random.randint(1, 10)
    match scenario:
        case 1:
            return "Still breathing Huh ?"
        case 2:
            return "Looks like you've got a guardian angel."
        case 3:
            return "You made it through. Impressive"
        case 4 | 5 | 6:
            return "Your slot was empty."
        case _ :
            return "Luck is on your side tonight."


def clear_terminal() -> None:
    """
    clear the terminal
    """
    if os.name == "posix": # Unix
        os.system("clear")
    else: # Windows
        os.system("cls")


def ask_play():
    """
    ask one last time to the user if he want to play
    """
    clear_terminal()
    print("DEALER:")
    print_human('Are you sure you want to play ? [y] : ')
    return input("").lower() != 'y'


def papers_signed(edition: str, name: str) -> None:
    """
    remember the signed papers in papers/ directory
    """
    with open(f"papers/{edition}-{name}", mode="w+") as f:
        f.write("")

def ask_papers() -> bool:
    """
    ask papers
    """
    clear_terminal()
    if os.name == "posix": # Unix
        edition = "Linux"
    else: # Windows
        edition = "Windows"
    print("DEALER:")
    print_human(CONTRACT(edition) + "\n")
    print_human("SIGN RIGHT THERE -> ")
    name = input("")
    while not name or name.lower() == "dealer":
        if name.lower() == "dealer":
            print_human("Please use your real name\n")
        print_human("SIGN RIGHT THERE -> ")
        name = input("")
    papers_signed(edition, name)
    return edition


def display(free: set, bullet: int = None) -> None:
    """
    display in the terminal the free spots that are in the arg
    """
    for e in range(1, 7):
        if e == bullet:
            print(f"\033[91m{e} ██\033[0m", end="\t")  
        elif e in free:
            print(f"{e} ██", end="\t")
        else:
            print(f"{'\u0336'.join(str(e)) + '\u0336'} ░░", end="\t")
    print()


def dealer_dies():
    time.sleep(2)
    print_human("I died...\n")
    time.sleep(1.5)
    print_human("That's weird.\n")
    time.sleep(5)
    print_human("How can you die twice ?")
    time.sleep(1) 
    print_human(" There is no way\n")
    with open(".dealer_status", mode="w+") as f:
        f.write("dead?")
    exit(0)


def round() -> bool:
    """
    execute one round of russian roulette
    """
    rand = random.randint(1, 6)
    free = set(range(1, 7))
    while True:
        clear_terminal()
        display(free)
        choice = input(f"Select a slot {list(free)} -> ")
        while not choice or not choice.isdecimal() or int(choice) not in free:
            clear_terminal()
            display(free)
            choice = input(f"Select a slot {list(free)} -> ")
        if int(choice) == rand:
            clear_terminal()
            display(free, rand)
            print_human("You died\n")
            return True
        else:
            free.remove(int(choice))
            clear_terminal()
            display(free)
            print_human(random_surviving_text() + "\n")
            time.sleep(2)
            print_human("My turn.\n")
            time.sleep(2)
            rand2 = random.choice(list(free))
            print_human(f"I selected the slot n°{rand2}.\n")
            time.sleep(1)
            if rand2 == rand:
                clear_terminal()
                display(free, rand)
                print("My turn")
                print(f"I selected the slot n°{rand2}.")
                dealer_dies()
            else:
                print_human("The slot didn't seem to have a bullet.\n")
                free.remove(rand2)
                time.sleep(2)
    return False


def check_dealer_status() -> None:
    """
    check if the dealer is 'ready' to play
    """
    try:
        with open(".dealer_status", mode="r") as f:
            status = f.read()
            assert  status != "dead?"
    except Exception:
        for _ in range(3):
            clear_terminal()
            time.sleep(0.4)
            print("You wan't to play but nobody is there.")
            time.sleep(0.9)
        exit()
    else:
        return

def main():
    """
    run the program
    """
    loading_screen.show_title(debug_mode=False)
    check_dealer_status()
    i_want_to_live = ask_play()
    if (i_want_to_live):
        print_human("Good decision.")
        return
    else:
        os_name = ask_papers()

    dead = False
    while (not dead):
        dead = round()
    os.system(f"python3 source/dying.py {os_name} &")

if __name__ == "__main__":
    main()