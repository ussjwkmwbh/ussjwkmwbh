import random as rd
from time import sleep
MAX_BULLETS = 6
num_bullets = 1
def yap_rules(num_of_bullets, max_capacity):
    print(f"This game consists of a Revolver and {num_of_bullets} bullet out of {max_capacity} in capacity")
    print("If The Revolver Fires the real Bullet. You will Lose.")
    print(f"chance of losing: {num_of_bullets}/{max_capacity}")
    print(f"chance of winning: {max_capacity-num_of_bullets}/{max_capacity}")

def yap_gun():
    sleep(1)
    print("Bullet Loaded..")
    sleep(1)
    print("Cartrige Rotated..")
    sleep(1)
    print("Trigger Pulled")
    sleep(2)

def shoot(num_fav_outcomes=num_bullets, num_total_outcomes=MAX_BULLETS):
    if rd.randint(num_fav_outcomes, num_total_outcomes) == 6:
        return True
    else:
        return False 
def main():
    print("Welcome, This is Russian Roullte.")
    print("Enter 'r' to know rules or Enter any key to continue:",end=' ')
    response = input()
    if response.lower() != 'r':
        print("You know the rules, so do I, Let's not say goodbye!")
    else:
        yap_rules(num_bullets,MAX_BULLETS)
        
    input("Press any key to shoot: ")
    yap_gun()
    if shoot(num_bullets, MAX_BULLETS):
        print("You Lose, you shot a real bullet")
    else:
        print("You WIN! you survived")

if __name__ == '__main__':
    main()
    input()