import os
import time

def clear_screen(func):
    def wrapper(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        return func(*args, **kwargs)
    return wrapper

@clear_screen
def panel():
    print("Press Given Key for the Respective Functionality.")
    print("A: Start the Election.")
    print("B: Ballot.")
    print("T: Get total number of votes.")
    print("S: Stop the Election.")
    choice = str(input())
    if choice.upper() == 'A':
        return 'start'
    elif choice.upper() == 'B':
        return 'ballot'
    elif choice.upper() == 'T':
        return 'total'
    elif choice.upper() == 'S':
        return 'stop'
    else:
        return 'invalid'
    
def main():
    read_signal = None
    print_token = True
    if os.name == 'nt':
        os.system('start ./lil_projects/EVM/Polling_booth.py')
    else:
        os.system('python3 ./lil_projects/EVM/Polling_booth.py &')
    wireIn = open('./lil_projects/EVM/communicator.txt', 'r')
    if wireIn.read() == '':
        wireIn.close()
        print("closed")
        wireOut=open('./lil_projects/EVM/communicator.txt', 'w')
        wireOut.write(panel())
        wireOut.close()
    else:
        wireIn.close()
        wireOut=open('./lil_projects/EVM/communicator.txt', 'w')
        wireOut.write('start')
        wireOut.close()    
        
    while True:
        wireIn = open('./lil_projects/EVM/communicator.txt', 'r')
        read_signal = wireIn.read()
        wireIn.close()
        if read_signal == 'ballot':
            pass
        elif read_signal == 'busy':
            if print_token == True:
                print("Ballot unit is busy")
                print_token = False
        elif read_signal == 'voted':
            print_token = True
            print("The Vote has been casted.")
            with open('./lil_projects/EVM/communicator.txt', 'w') as wireOut:
                wireOut.write(panel())    
        elif read_signal == 'start':
            with open('./lil_projects/EVM/communicator.txt', 'w') as wireOut:
                wireOut.write(panel())     
        elif read_signal == 'stop':
            break    
        elif read_signal.isdigit():
            print("Total Votes: ", read_signal)
            time.sleep(3)
            with open('./lil_projects/EVM/communicator.txt', 'w') as wireOut:
                wireOut.write(panel())
        elif read_signal == 'invalid':
            print("Invalid Input.")
            time.sleep(3)
            with open('./lil_projects/EVM/communicator.txt', 'w') as wireOut:
                wireOut.write(panel())
        

                
    
    
if __name__=='__main__':
    main()