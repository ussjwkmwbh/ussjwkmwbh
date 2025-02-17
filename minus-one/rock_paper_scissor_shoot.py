import stone_paper_scissor as rps
import russian_roullete as rr
from os import system

def change(choice, choices):
    if choice == 'r':
        choice = choices[0]
    elif choice == 'p':
        choice = choices[1]
    elif choice == 's':
        choice = choices[2]
    else:
        return None
    
    return choice
def main():
    num_bullets=1
    run = True
    choices = rps.choices
    health = p1_hp = p2_hp = 1
    shot = None
    while run:
        while True:
            print("Player 1")
            choice = input("Enter a object(r/p/s): ").lower()
            if choice == 'r' or choice == 'p' or choice == 's':
                break
            else:
                print('Write Valid Input\a')
        choice_1 = change(choice, choices)

        system("cls")

        while True:
            print("Player 2")
            choice = input("Enter a object(r/p/s): ").lower()
            if choice == 'r' or choice == 'p' or choice == 's':
                break
            else:
                print('Write Valid Input\a')
        choice_2 = change(choice, choices)

        system('cls')

        result = rps.findWinner(choice_1,choice_2)
        print("<<",choice_1,"VS",choice_2,">>")
        input()
        if result == 'T':
            if num_bullets < 6:
                num_bullets += 1
                print("It's a Tie, number of bullets increased")
            else:
                print("It is a Tie.")

        elif result == '1' or result == '2':
            rr.yap_gun()
            shot = rr.shoot(num_bullets)
            print('Bullet Shot' if shot else 'No Bullet shot')
        
        if shot and (result == '1' or result == '2'):
            run = False
        else:
            continue

    if result == '1':
        print("Player 1 wins")
    elif result == '2':
        print("Player 2 wins")
    
if __name__ == '__main__':
    main()