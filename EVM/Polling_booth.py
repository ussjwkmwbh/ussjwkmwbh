from os import system
import csv
import json
import time

def main():
    # Read the CSV file and store candidate data
    with open(r'lil_projects\EVM\candidates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        candidates = list(reader)  # Convert iterator to list for multiple uses
    """
    # Display candidates
    print("SL.NO | NAME OF CANDIDATE -- PARTY")
    for i, row in enumerate(candidates, 1):
        print(f"{i} | {row['candidate_name']} -- {row['party_name']}")
    """
    print("EVM Ballot Unit \nPlease wait for Control Unit.")
    # Infinite loop waiting for 'ballot' signal

    # Voting process
    votes = []
    poll_open = False
    while True:
        while True:
            with open('lil_projects/EVM/communicator.txt', 'r') as wire:
                wireIn = wire.read().strip()
                if wireIn == 'ballot':  # Strip to remove unwanted spaces
                    poll_open = True
                    break  # Exit loop when 'ballot' is detected
                if wireIn == 'stop':
                    poll_open = False
                    break
                if wireIn == 'total':
                    poll_open = False
                    break

            time.sleep(0.5)  # Prevent excessive file reads (reduce CPU usage)
        if poll_open:
            while poll_open:
                try:
                    print("SL.NO | NAME OF CANDIDATE -- PARTY")
                    for i, row in enumerate(candidates, 1):
                        print(f"{i} | {row['candidate_name']} -- {row['party_name']}")

                    with open('lil_projects/EVM/communicator.txt', 'w') as wire:
                        wire.write('busy')
                    choice = int(input("Enter the Sl.no of Favourable Candidate: "))

                    if 1 <= choice <= len(candidates):
                        votes.append(choice); lst = candidates[choice-1]
                        print(f"Candidate Name: {lst['candidate_name']}\nParty Name: {lst['party_name']}") 
                        time.sleep(3)
                        system('cls')
                            # Update communicator.txt
                        with open('lil_projects/EVM/communicator.txt', 'w') as wire:
                            wire.write("voted")
                        poll_open = False
                    else:
                        print("Please Enter a Valid Input.")
                        time.sleep(2)
                        system('cls')
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    time.sleep(2)
                    system('cls')
        #print(votes)
        if wireIn == 'stop':
            break
        if wireIn == 'total':
            with open('lil_projects/EVM/communicator.txt', 'w') as wire:
                wire.write(str(len(votes)))

    votes.sort()
    counter_dict = {}
    for num in range(1, len(candidates) + 1):
        counter_dict[num] = 0

    for num in votes:
        if num in counter_dict:
            counter_dict[num] += 1
            
    counter_dict['total_votes'] = len(votes)
    counter_dict['total_candidates'] = len(candidates)

    
    with open('lil_projects/EVM/votes.json', 'w') as file:
        json.dump(counter_dict, file, indent=4)

    print("Poll has been closed and saved")
    time.sleep(3)

if __name__ == '__main__':
    main()
