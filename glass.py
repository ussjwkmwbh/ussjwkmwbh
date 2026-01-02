import random
from os import system

class Glass:
    @staticmethod
    def draw(direction=None):
        if direction == 'left' or direction == 'l':
            print("|----||----|")
            print("| ## ||    |")
            print("|----||----|")
        elif direction == 'right' or direction == 'r':
            print("|----||----|")
            print("|    || ## |")
            print("|----||----|")
        else:
            print("|----||----|")
            print("|    ||    |")
            print("|----||----|")
    
    @staticmethod
    def draw_border(direction='up'):
        if direction=='up':
            print("____________")
        elif direction=='down':
            print("‾‾‾‾‾‾‾‾‾‾‾‾")
        

    @staticmethod
    def draw_broke(direction):
        if direction == 'right' or direction == 'r':
            print("|----||   /|")
            print("|    ||  / |")
            print("|----|| /  |")
        elif direction == 'left' or direction == 'l':
            print(r"| \  ||----|")
            print(r"|  \ ||    |")
            print(r"|   \||----|")
        else:
            pass

# Initialize number of stages
no_of_stages = 3

# Initialize glasses and pairs
no_of_glasses = no_of_stages * 2
glasses = list(range(1, no_of_glasses + 1))
glass_pair = [(glasses[i], glasses[i + 1]) for i in range(0, len(glasses) - 1, 2)]

# Determine breakable glasses
breakables = [random.choice(pair) for pair in glass_pair]

# Number of stages
num_stages = len(glass_pair)
status = None
break_permit = False
# Main loop for stages
for stage in range(num_stages):
    system('cls')  # Clear the console
    Glass.draw_border()  # Draw the top border
    if stage == 0:
        for n in range(num_stages):
            Glass.draw()  # Draw all glasses initially
    else:
        for n in range(num_stages, 0, -1):
            if n == stage:
                if status == 'left_stepped':
                    Glass.draw('left')
                elif status == 'right_stepped':
                    Glass.draw('right')
                elif status == 'left_broke':
                    Glass.draw_broke('left')
                    break_permit = True
                elif status == 'right_broke':
                    Glass.draw_broke('right')
                    break_permit = True
                else:
                    Glass.draw()
            else:
                Glass.draw()
    Glass.draw_border('down')  # Draw the bottom border
    if break_permit:
        break
    print("Stage ", stage + 1)
    while True:
        #print(*breakables)
        select = int(input("Select Left(1) or Right(2) Glass (1/2): "))
        if 1<=select<=2:
            break
        else:
            print("Invalid Input. Select Again.")
    glass = glass_pair[stage]

    if select == 1:
        option = glass[0]
        status = 'left_stepped'
    elif select == 2:
        option = glass[1]
        status = 'right_stepped'
    else:
        continue

    if option in breakables:
        if status == 'left_stepped':
            status = 'left_broke'
        elif status == 'right_stepped':
            status = 'right_broke'

n = 1
#Check wheter the player won or lose
if option not in breakables:
    Glass.draw_border()
    system('cls')  # Clear the console
    if status == 'left_stepped':
        Glass.draw('left')
    elif status == 'right_stepped':
        Glass.draw('right')
    
    while n < num_stages:
        Glass.draw()
        n += 1
    Glass.draw_border('down')

    print("You Won")

else:
    if option is breakables[-1]: # Checks if the wrong option is last one
        system('cls')  # Clear the console
        Glass.draw_border()
        if status == 'left_broke':
            Glass.draw_broke('left')
        elif status == 'right_broke':
            Glass.draw_broke('right')
        while n < num_stages:
            Glass.draw()
            n += 1
        Glass.draw_border('down')

    print("You Lose")

print("Breakables: ",*breakables,end="")    
input()