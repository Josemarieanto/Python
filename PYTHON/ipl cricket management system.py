# # # print("WELCOME TO IPL CRICKET🎉")

# # # # Input the owners and teams in the format: owner1 team1 owner2 team2 ...
# # # data = input("Enter the owners and teams: ").split()

# # # # Convert the input list into a dictionary by pairing items
# # # owners = dict(zip(data[::2], data[1::2]))

# # # print(owners)


# # class IPLCricketManagementSystem:
# #     def __init__(self):
# #         self.teams = {}
    
# #     def add_team(self, owner, team):
# #         if team in self.teams:
# #             print(f"Team {team} already exists. Owner is {self.teams[team]}.")
# #         else:
# #             self.teams[team] = owner
# #             print(f"Added team {team} with owner {owner}.")
    
# #     def view_teams(self):
# #         if not self.teams:
# #             print("No teams available.")
# #         else:
# #             print("Teams and their owners:")
# #             for team, owner in self.teams.items():
# #                 print(f"Team: {team}, Owner: {owner}")
    
# #     def find_owner(self, team):
# #         owner = self.teams.get(team)
# #         if owner:
# #             print(f"The owner of team {team} is {owner}.")
# #         else:
# #             print(f"Team {team} does not exist.")

# # def main():
# #     system = IPLCricketManagementSystem()
    
# #     while True:
# #         print("\n1. Add Team")
# #         print("\n2. View Teams")
# #         print("\n3. Find Owner")
# #         print("\n4. Exit")
# #         choice = input("Enter your choice: ")
        
# #         if choice == '1':
# #             owner = input("Enter the owner name: ")
# #             team = input("Enter the team name: ")
# #             system.add_team(owner, team)
# #         elif choice == '2':
# #             system.view_teams()
# #         elif choice == '3':
# #             team = input("Enter the team name: ")
# #             system.find_owner(team)
# #         elif choice == '4':
# #             print("Exiting the IPL Cricket Management System.")
# #             break
# #         else:
# #             print("Invalid choice, please try again.")

# # if __name__ == "__main__":
# #     main()


# # import random

# # def add_team(teams):
# #     owner = input("Enter the owner name: ")
# #     team = input("Enter the team name: ")
# #     if team in teams:
# #         print(f"Team {team} already exists. Owner is {teams[team]['owner']}.")
# #     else:
# #         teams[team] = {'owner': owner, 'players': []}
# #         print(f"Added team {team} with owner {owner}.")

# # def view_teams(teams):
# #     if not teams:
# #         print("No teams available.")
# #     else:
# #         print("Teams and their owners:")
# #         for team, info in teams.items():
# #             print(f"Team: {team}, Owner: {info['owner']}, Players: {', '.join(info['players'])}")

# # def find_owner(teams):
# #     team = input("Enter the team name: ")
# #     info = teams.get(team)
# #     if info:
# #         print(f"The owner of team {team} is {info['owner']}.")
# #     else:
# #         print(f"Team {team} does not exist.")

# # def conduct_auction(teams, players, player_prices):
# #     for player in players:
# #         print(f"\nAuctioning player: {player} (Price: {player_prices[player]})")
# #         bids = {}
# #         for team in teams:
# #             if len(teams[team]['players']) < 5:
# #                 bid = input(f"Enter bid for team {team} (or press Enter to skip): ")
# #                 if bid:
# #                     bids[team] = int(bid)
        
# #         if bids:
# #             winning_team = max(bids, key=bids.get)
# #             teams[winning_team]['players'].append(player)
# #             print(f"{player} is allocated to team {winning_team} with a bid of {bids[winning_team]}")
# #         else:
# #             print(f"No bids for player {player}. Player remains unallocated.")

# # def main():
# #     teams = {}
# #     players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"]
# #     player_prices = {player: random.randint(100, 500) for player in players}
    
# #     while True:
# #         print("\n1. Add Team")
# #         print("2. View Teams")
# #         print("3. Find Owner")
# #         print("4. Conduct Auction")
# #         print("5. Exit")
# #         choice = input("Enter your choice: ")
        
# #         if choice == '1':
# #             add_team(teams)
# #         elif choice == '2':
# #             view_teams(teams)
# #         elif choice == '3':
# #             find_owner(teams)
# #         elif choice == '4':
# #             conduct_auction(teams, players, player_prices)
# #         elif choice == '5':
# #             print("Exiting the IPL Cricket Management System.")
# #             break
# #         else:
# #             print("Invalid choice, please try again.")

# # if __name__ == "__main__":
# #     main()


# import random

# def add_team(teams):
#     owner = input("Enter the owner name: ")
#     team = input("Enter the team name: ")
#     if team in teams:
#         print(f"Team {team} already exists. Owner is {teams[team]['owner']}.")
#     else:
#         teams[team] = {'owner': owner, 'players': [], 'budget': 2000}
#         print(f"Added team {team} with owner {owner} and a budget of 2000.")

# def view_teams(teams):
#     if not teams:
#         print("No teams available.")
#     else:
#         print("Teams and their owners:")
#         for team, info in teams.items():
#             players = ', '.join(info['players']) if info['players'] else 'No players yet'
#             print(f"Team: {team}, Owner: {info['owner']}, Budget: {info['budget']}, Players: {players}")

# def find_owner(teams):
#     team = input("Enter the team name: ")
#     info = teams.get(team)
#     if info:
#         print(f"The owner of team {team} is {info['owner']}.")
#     else:
#         print(f"Team {team} does not exist.")

# def conduct_auction(teams, players, player_prices):
#     for player in players:
#         print(f"\nAuctioning player: {player} (Price: {player_prices[player]})")
#         bids = {}
#         for team, info in teams.items():
#             if len(info['players']) < 5 and info['budget'] >= player_prices[player]:
#                 bid = input(f"Enter bid for team {team} (or press Enter to skip): ")
#                 if bid:
#                     bid = int(bid)
#                     if bid <= info['budget']:
#                         bids[team] = bid
#                     else:
#                         print(f"Bid exceeds the budget for team {team}.")
        
#         if bids:
#             winning_team = max(bids, key=bids.get)
#             teams[winning_team]['players'].append(player)
#             teams[winning_team]['budget'] -= player_prices[player]
#             print(f"{player} is allocated to team {winning_team} with a bid of {bids[winning_team]}")
#         else:
#             print(f"No valid bids for player {player}. Player remains unallocated.")

#     # Ensure all teams have exactly 5 players
#     unallocated_players = [player for player in players if not any(player in info['players'] for info in teams.values())]
#     for team, info in teams.items():
#         while len(info['players']) < 5 and unallocated_players:
#             player = unallocated_players.pop(0)
#             info['players'].append(player)
#             print(f"{player} has been forcibly allocated to team {team} to meet the 5 player requirement.")

# def main():
#     teams = {}
#     players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"]
#     player_prices = {player: random.randint(100, 500) for player in players}
    
#     while True:
#         print("\n1. Add Team")
#         print("2. View Teams")
#         print("3. Find Owner")
#         print("4. Conduct Auction")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == '1':
#             add_team(teams)
#         elif choice == '2':
#             view_teams(teams)
#         elif choice == '3':
#             find_owner(teams)
#         elif choice == '4':
#             conduct_auction(teams, players, player_prices)
#         elif choice == '5':
#             print("Exiting the IPL Cricket Management System.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()


import random

def add_team(teams):
    if len(teams) >= 6:
        print("Cannot add more teams. Only 6 teams are allowed.")
        return

    owner = input("Enter the owner name: ")
    team = input("Enter the team name: ")
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

def main():
    teams = {}
    players = [f"Player{i}" for i in range(1, 31)]  # 30 players
    player_prices = {player: random.randint(100, 500) for player in players}
    
    while True:
        print("\n1. Add Team")
        print("2. View Teams")
        print("3. Find Owner")
        print("4. Conduct Auction")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_team(teams)
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
            print("Exiting the IPL Cricket Management System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
