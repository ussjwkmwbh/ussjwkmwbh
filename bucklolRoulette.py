from random import choice, randint

# Function to display health of both players
def show_health(p1, p2):  
    print(f"Player 1 Health: {p1}\nPlayer 2 Health: {p2}")

# Function to display the number of real and fake bullets
def show_bullets(num_real_bullets, num_fake_bullets):  
    capacity = max_capacity  # Total capacity of the gun
    # Ensure the bullets do not exceed gun capacity
    if capacity < num_real_bullets + num_fake_bullets:
        return False
    else:
        print(f"There are {num_real_bullets} real and {num_fake_bullets} fake bullets")

# Function to simulate firing the gun
def gun(num_real_bullets, num_fake_bullets):
    fake_bullet, real_bullet = 0, 1  # Fake bullet is represented by 0, real bullet by 1

    while num_real_bullets != 0:  # As long as there are real bullets
        if num_fake_bullets != 0:  # If there are fake bullets, choose randomly
            bullet = choice((fake_bullet, real_bullet))
        else:  # If only real bullets remain, it always fires real
            bullet = real_bullet
            return True

        if bullet == real_bullet:  # Fired a real bullet
            return True
        elif bullet == fake_bullet:  # Fired a fake bullet
            return False
    print("Gun is Empty.")  # No bullets remain
    return None

# Function to determine the outcome of a shot
def shoot(option, num_real_bullets, num_fake_bullets):
    if option == 0:  # Player chooses to shoot themselves
        if gun(num_real_bullets, num_fake_bullets) == True:
            print("You shot a real bullet. Your health point decreased.")
            return 'self_fired'
        else:
            print("You fired a fake bullet.")
            return 'false_fired'
    elif option == 1:  # Player chooses to shoot the opponent
        if gun(num_real_bullets, num_fake_bullets) == True:
            print("You shot a real bullet. Opponent's health point decreased.")
            return 'enemy_fired'
        else:
            print("You fired a fake bullet. Opponent gets a chance.")
            return 'enemy_missed'

# Function to check if a player has won
def checkWin(p1, p2):
    if p1 == 0:  # Player 1's health is zero
        return 2  # Player 2 wins
    elif p2 == 0:  # Player 2's health is zero
        return 1  # Player 1 wins
    else:
        return None  # Game continues

# Game initialization
num_lives = 2  # Each player starts with 2 health points
p1, p2 = num_lives, num_lives
max_capacity = 6  # Gun can hold up to 6 bullets

# Randomly determine the number of real and fake bullets
num_real_bullets = randint(1, max_capacity)
num_fake_bullets = max_capacity - num_real_bullets

# Main game loop
run = True
while run:
    # Show player health and bullet count
    show_health(p1, p2)
    show_bullets(num_real_bullets, num_fake_bullets)

    # Player 1's turn
    p_chance = 1
    while p_chance == 1:
        print("For Player 1:")
        option = int(input("Press 1 to shoot Player 2 or Press 0 to shoot self: "))
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

    # Check for a winner
    declare = checkWin(p1, p2)
    if declare == 1:
        print("Player 1 Wins.")
        break
    elif declare == 2:
        print("Player 2 Wins.")
        break

    # Player 2's turn
    show_health(p1, p2)
    show_bullets(num_real_bullets, num_fake_bullets)
    p_chance = 1
    while p_chance == 1:
        print("For Player 2:")
        option = int(input("Press 1 to shoot Player 1 or Press 0 to shoot self: "))
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

    # Check for a winner
    declare = checkWin(p1, p2)
    if declare == 1:
        print("Player 1 Wins.")
        break
    elif declare == 2:
        print("Player 2 Wins.")
        break

print("THANK YOU. PLS COME AGAIN")

