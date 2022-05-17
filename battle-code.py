import os
from time import sleep


def line():
    print('-='*35)


def space():
    print(' ')


def Charmeleon():

    line()
    print('Chosen Pokemon CHARMELEON')
    space()
    print(
        f'=> Life: {LifePokemon}\n=> Attack: {AttackPokemon}\n=> Cure: {CurePokemon}')
    line()
    return


def Ivysaur():

    line()
    print('Chosen Pokemon Ivysaur')
    space()
    print(
        f'=> Life: {LifePokemon}\n=> Attack: {AttackPokemon}\n=> Cure: {CurePokemon}')
    line()
    return


def Wartotle():

    line()
    print('Chosen Pokemon Wartotle')
    space()
    print(
        f'=> Life: {LifePokemon}\n=> Attack: {AttackPokemon}\n=> Cure: {CurePokemon}')
    line()
    return


def Lugia():
    sleep(0.3)
    print("Boss: Lugia")
    space()

    sleep(0.3)
    print(f"=> Life = {lifeLugia}")
    sleep(0.3)
    print(f'=> Attack = {attackLugia}')
    line()


def proceed():
    print('Are you sure of your choice?')

    certain = input('Write yes or no: ').lower()
    return certain


def end():
    if LifePokemon <= 0:
        line()
        space()
        print(
            f'{player}, You lost the battle!!\nLugia has defeated you. PLAYER DIFF HAHAHA')
        space()
        line()

    elif lifeLugia <= 0:
        line()
        space()
        print(f'GG WP {player}, you defeated the boss. TOO EASY!!')
        space()
        line()


def clearTerminal():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


certain = "no"
restart = "yes"

clearTerminal()

space()
sleep(0.3)
print('Welcome to pokemon battle')
space()

sleep(0.6)
player = input('Write your nickname: ').upper()
print(f"let's move on, trainer {player}")
sleep(0.8)

clearTerminal()

while restart == "yes":
    lifeLugia = 300
    attackLugia = 50

    while certain == "no":
        sleep(0.7)
        print(f'Choose your pokemon for battle')
        space()

        line()
        print("A - Charmeleon\n\n> Life: 140\n> Attack: 70\n> Cure: 60")

        line()
        print("B - Wartotle\n\n> Life: 180\n> Attack: 65\n> Cure: 65")

        line()
        print("C - Ivysaur\n\n> Life: 160\n> Attack: 65\n> Cure: 80")

        space()
        choice = input("=> ").lower()

        clearTerminal()

        sleep(0.5)
        if choice == 'a':
            pokemon = "Charmeleon"
            LifePokemon = 140
            AttackPokemon = 70
            CurePokemon = 55

            Charmeleon()

            certain = proceed()

        elif choice == 'b':
            pokemon = "Wartole"
            LifePokemon = 180
            AttackPokemon = 65
            CurePokemon = 60

            Wartotle()

            certain = proceed()

        elif choice == 'c':
            pokemon = "Ivysaur"
            LifePokemon = 160
            AttackPokemon = 65
            CurePokemon = 70

            Ivysaur()

            certain = proceed()

        else:
            space()
            print('Wrong option friend, TRY AGAIN')
            space()

    space()

    clearTerminal()

    sleep(0.3)
    print("NOW IT'S DUEL TIME")
    space()
    sleep(0.3)
    print("ops... wrong game >_<")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print("NOW IS BATTLE TIME")
    space()

    line()
    sleep(0.3)
    print("A wild Lugia appears!!")
    space()

    Lugia()

    space()
    sleep(0.3)
    battle = input(f"Want to start now?? yes/no\n=> ").lower()

    clearTerminal()

    space()
    print(f'{pokemon}, I choose you!')

    if battle == "no":
        break

    elif battle != "yes" and "no":
        print("HAHAHA Wrong option but now you will fight")

    while LifePokemon > 0 and lifeLugia > 0:
        battle = "yes"

        while battle == "yes":
            line()
            sleep(0.3)
            choiceShift = input(
                f"What {pokemon} should do?\n\nA - Attack\nB - Cure\n=> ").upper()
            space()

            if choiceShift == "A":
                lifeLugia = lifeLugia - AttackPokemon

                if lifeLugia < 0:
                    lifeLugia = 0

                sleep(0.5)
                print(
                    f"You attacked and dealt {AttackPokemon} damage\n=> Boss's remaining life: {lifeLugia} Life")
                space()

                battle = "no"

            elif choiceShift == "B":
                LifePokemon = LifePokemon + CurePokemon
                if LifePokemon < 0:
                    LifePokemon = 0

                sleep(0.5)
                print(
                    f'You healed with {CurePokemon} health\n=> and now has {LifePokemon} health')
                space()
                battle = "no"

            else:
                sleep(0.3)
                print("Wrong option friend")
                space()

                sleep(0.3)
                print("But you missed the shift")
                space()
                battle = "no"

        if lifeLugia >= 0:
            if lifeLugia == 0:
                break

            LifePokemon = LifePokemon - attackLugia

            if LifePokemon <= 0:
                LifePokemon = 0

            line()
            sleep(0.3)
            print(f"Lugia attacked you and dealt you {attackLugia} damage")

            sleep(0.3)
            print(f'=> Your remaining life: {LifePokemon}')
            sleep(3)

            clearTerminal()

            space()

    clearTerminal()

    end()

    sleep(2.5)

    clearTerminal()

    restart = input("Want to try again? (Write yes or no)\n=> ").lower()

    if restart == "yes":
        certain = "no"

    elif restart == "no":
        space()
        break

    else:
        space()
        print("GOOD TRY HAHAHA\n\nBYE...")
        break

clearTerminal()
line()
space()
sleep(0.5)

print(f"Thanks for testing my program, trainer {player}")
sleep(0.3)
print("github: https://github.com/socramcz")

space()
line()
sleep(3.5)
