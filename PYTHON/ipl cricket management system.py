import random
from itertools import combinations, product

def add_teams_bulk(teams):
    if len(teams) + 6 > 6:
        print("Cannot add more teams. Only 6 teams are allowed in total.")
        return
    
    for i in range(6):
        owner = input(f"Enter the owner name for team {i+1}: ")
        team = input(f"Enter the team name for team {i+1}: ")
        if team in teams:
            print(f"Team {team} already exists. Owner is {teams[team]['owner']}.")
        else:
            teams[team] = {'owner': owner, 'players': [], 'budget': 2000}
            print(f"Added team {team} with owner {owner} and a budget of 2000.")

def view_teams(teams):
    if not teams:
        print("No teams available.")
    else:
        print("Teams and their owners:")
        for team, info in teams.items():
            players = ', '.join(info['players']) if info['players'] else 'No players yet'
            print(f"Team: {team}, Owner: {info['owner']}, Budget: {info['budget']}, Players: {players}")

def find_owner(teams):
    team = input("Enter the team name: ")
    info = teams.get(team)
    if info:
        print(f"The owner of team {team} is {info['owner']}.")
    else:
        print(f"Team {team} does not exist.")

def conduct_auction(teams, players, player_prices):
    unallocated_players = list(players)  # Make a copy of the players list

    for player in players:
        print(f"\nAuctioning player: {player} (Price: {player_prices[player]})")
        bids = {}
        for team, info in teams.items():
            if len(info['players']) < 5 and info['budget'] >= player_prices[player]:
                bid = input(f"Enter bid for team {team} (or press Enter to skip): ")
                if bid:
                    bid = int(bid)
                    if bid <= info['budget']:
                        bids[team] = bid
                    else:
                        print(f"Bid exceeds the budget for team {team}.")
        
        if bids:
            winning_team = max(bids, key=bids.get)
            teams[winning_team]['players'].append(player)
            teams[winning_team]['budget'] -= player_prices[player]
            unallocated_players.remove(player)
            print(f"{player} is allocated to team {winning_team} with a bid of {bids[winning_team]}")
        else:
            print(f"No valid bids for player {player}. Player remains unallocated.")

    # Ensure all teams have exactly 5 players
    for team, info in teams.items():
        while len(info['players']) < 5 and unallocated_players:
            player = unallocated_players.pop(0)
            info['players'].append(player)
            print(f"{player} has been forcibly allocated to team {team} to meet the 5 player requirement.")

def generate_schedule(teams):
    if len(teams) != 6:
        print("Schedule can only be generated when there are exactly 6 teams.")
        return

    team_list = list(teams.keys())
    random.shuffle(team_list)
    group_a = team_list[:3]
    group_b = team_list[3:]

    schedule = []

    # Matches within Group A
    for match in combinations(group_a, 2):
        schedule.append((match[0], match[1]))

    # Matches within Group B
    for match in combinations(group_b, 2):
        schedule.append((match[0], match[1]))

    # Matches between Group A and Group B
    for match in product(group_a, group_b):
        schedule.append((match[0], match[1]))

    print("\nMatch Schedule:")
    for i, match in enumerate(schedule, 1):
        print(f"Match {i}: {match[0]} vs {match[1]}")

def main():
    teams = {}
    players = [f"Player{i}" for i in range(1, 31)]  # 30 players
    player_prices = {player: random.randint(100, 500) for player in players}
    
    while True:
        print("\n1. Add Team")
        print("2. View Teams")
        print("3. Find Owner")
        print("4. Conduct Auction")
        print("5. Generate Schedule")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_teams_bulk(teams)
        elif choice == '2':
            view_teams(teams)
        elif choice == '3':
            find_owner(teams)
        elif choice == '4':
            if len(teams) != 6:
                print("Auction can only be conducted when there are exactly 6 teams.")
            else:
                conduct_auction(teams, players, player_prices)
        elif choice == '5':
            generate_schedule(teams)
        elif choice == '6':
            print("Exiting the IPL Cricket Management System.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
