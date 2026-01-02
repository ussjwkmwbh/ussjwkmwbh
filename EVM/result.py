import csv
import json

def list_candidates(candidates, votes):
    print("Candidate Name (Party Name) : Vote Count")
    for i in range(1, votes['total_candidates']+1):
        candidate_index = str(i)
        candidate_name = candidates[i-1]['name']
        party_name = candidates[i-1]['party']
        vote_count = votes.get(candidate_index, 0)
        print(f"{candidate_name} ({party_name}) : {vote_count}")

    print("\nTotal Votes: ", votes['total_votes'])



def main():
    candidates = []
    with open(r'lil_projects\EVM\candidates.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                candidates.append({
                        'name': row['candidate_name'],
                        'party': row['party_name'],
                })

    with open(r'lil_projects\EVM\votes.json', 'r') as file:
        votes = json.load(file)

    candidate_votes = []
    for i in range(1, votes['total_candidates'] + 1):
        candidate_index = str(i)
        candidate_name = candidates[i-1]['name']
        party_name = candidates[i-1]['party']
        vote = votes.get(candidate_index, 0) # or votes[candidate_index] if candidate_index in votes else 0
        
        candidate_votes.append({
            'name': candidate_name,
            'party': party_name,
            'votes': vote
        })
    
    highest_votes = max(vote['votes'] for vote in candidate_votes)
    winners = []
    for candidate in candidate_votes:
        if candidate['votes'] == highest_votes:
            winners.append(candidate)

    with open(r'lil_projects\EVM\final_results.json', 'w') as file:
        json.dump(candidate_votes,file,indent=4)
    list_candidates(candidates, votes)

    if len(winners) == 1:
        winner = winners[0]
        print(f"\nThe winner is: {winner['name']} ({winner['party']}) with {winner['votes']} votes.")
    else:
        print(f"\nThere is a Tie, the following candidates recieved {highest_votes} each")
        for winner in winners:
            print(f"{winner['name']} ({winner['party']})")

if __name__ == "__main__":
    main()