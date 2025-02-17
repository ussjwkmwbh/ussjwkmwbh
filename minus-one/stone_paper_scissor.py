#include<python.h>
from os import system
"""/*
 PLAYER VS PLAYER
    STONE VS PAPER => PAPER
    STONE VS SCISSOR => SCISSOR
    STONE VS STONE => TIE

    PAPER VS STONE => PAPER
    PAPER VS SCISSOR => SCISSOR
    PAPER VS PAPER => TIE

    SCISSOR VS PAPER => SCISSOR
    SCISSOR VS STONE => STONE
    SCISSOR VS SCISSOR => SCISSOR
*/"""
choices = ['rock','paper','scissor']

def findWinner(obj_1,obj_2):
    if obj_1 == obj_2:
        return 'T'
    if (obj_1 == 'scissor' and obj_2=='paper') or (obj_1 == 'paper' and obj_2 == 'rock') or (obj_1 == 'rock' and obj_2 == 'scissor'):
        return '1'
    elif (obj_2 == 'scissor' and obj_1=='paper') or (obj_2 == 'paper' and obj_1 == 'rock') or (obj_2 == 'rock' and obj_1 == 'scissor'):
        return '2'
    else:
        return None
    
def main():
    while True:
        print("Player 1")
        choice = input("Enter a object(r/p/s): ").lower()
        if choice == 'r' or choice == 'p' or choice == 's':
            break
        else:
            print('Write Valid Input\a')
    if choice == 'r':
        choice_1 = choices[0]
    elif choice == 'p':
        choice_1 = choices[1]
    elif choice == 's':
        choice_1 = choices[2]
    else:
        return None
    system("cls")
    while True:
        print("Player 2")
        choice = input("Enter a object(r/p/s): ")
        if choice == 'r' or choice == 'p' or choice == 's':
            break
        else:
            print('Write Valid Input\a')
    if choice == 'r':
        choice_2 = choices[0]
    elif choice == 'p':
        choice_2 = choices[1]
    elif choice == 's':
        choice_2 = choices[2]
    else:
        return None
    
    print("<<",choice_1,"VS",choice_2,">>")

    w = findWinner(choice_1, choice_2)
    if w == 'T':
        print("<<TIE>>")
    elif w == '1':
        print("<<Player 1 Wins!>>")
    elif w == '2':
        print("<<Player 2 Wins>>")

if __name__ == '__main__':
    main()
    input()