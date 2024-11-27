from random import choice, randint
#BuckLol Roullete
def show_health(p1,p2): #Shows Health Stats
    print(f"Player 1 Health: {p1}\nPlayer 2 Health: {p2}")

def show_bullets(num_real_bullets, num_fake_bullets): 
    capacity = max_capacity
    if capacity < num_real_bullets+num_fake_bullets:
        return False
    else:
        print(f"There are {num_real_bullets} real and {num_fake_bullets} fake bullets")

def gun(num_real_bullets, num_fake_bullets):
    fake_bullet, real_bullet = 0, 1

    while num_real_bullets != 0:
        if num_fake_bullets != 0:
            bullet = choice((fake_bullet,real_bullet))
        else:
            bullet = real_bullet
            return True

        if bullet == real_bullet:
            return True

        elif bullet == fake_bullet:
            return False
    print("Gun is Empty.")

    return None

def shoot(option, num_real_bullets, num_fake_bullets):
    if option == 0:
        if gun(num_real_bullets, num_fake_bullets) == True:
            print("You Shot real bullet. Your Health point decreased")
            return 'self_fired'
        else:
            print("You fired a fake bullet.")
            return 'false_fired'
    elif option == 1:
        if gun(num_real_bullets, num_fake_bullets) == True:
            print("You shot a real bullet. Opponent's Health point decreased")
            return 'enemy_fired'
        else:
            print("You fired fake bullet. Opponent gets chance.")
            return 'enemy_missed'

def checkWin(p1, p2):
    if p1 == 0:
        return 2
    elif p2 == 0:
        return 1
    else:
        return None

num_lives = 2
p1, p2 = num_lives, num_lives
max_capacity = 6

num_real_bullets = randint(1, max_capacity)
num_fake_bullets = max_capacity-num_real_bullets

run = True

while run:
    show_health(p1,p2)
    show_bullets(num_real_bullets, num_fake_bullets)
    p_chance = 1 #OR p_chance = choice(0,1) //need to feed for initial time
    while p_chance == 1:
        print("For Player 1:")
        option = int(input("Press 1 to shoot Player 2 or Press 0 to shoot self"))
        chance = shoot(option, num_real_bullets, num_fake_bullets)
        if chance == 'self_fired':
            p1 -= 1
            num_real_bullets -= 1
            p_chance = 0
        elif chance == 'false_fired':
            num_fake_bullets -= 1

        elif chance == 'enemy_fired':
            p2 -= 1
            num_real_bullets -= 1
            p_chance = 0

        elif chance == 'enemy_missed':
            num_fake_bullets -= 1
            p_chance = 0

    declare = checkWin(p1,p2)
    if declare == 1:
        print("Player 1 Wins.")
        break

    elif declare == 2:
        print("Player 2 Wins.")
        break
    else:
        pass

    show_health(p1,p2)
    show_bullets(num_real_bullets, num_fake_bullets)
    p_chance = 1
    while p_chance == 1:
        print("For Player 2:")
        option = int(input("Press 1 to shoot Player 2 or Press 0 to shoot self"))
        chance = shoot(option, num_real_bullets, num_fake_bullets)
        if chance == 'self_fired':
            p2 -= 1
            num_real_bullets -= 1
            p_chance = 0
        elif chance == 'false_fired':
            num_fake_bullets -= 1

        elif chance == 'enemy_fired':
            p1 -= 1
            num_real_bullets -= 1
            p_chance = 0

        elif chance == 'enemy_missed':
            num_fake_bullets -= 1
            p_chance = 0


    declare = checkWin(p1,p2)
    if declare == 1:
        print("Player 1 Wins.")
        break

    elif declare == 2:
        print("Player 2 Wins.")
        break
    else:
        pass

print("THANK YOU. PLS COME AGAIN")