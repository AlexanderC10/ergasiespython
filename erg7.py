import requests
from datetime import datetime

date = input("Select final date of month (format YYYY-MM-DD): ")
num_games = int(input("Select number of games to check (191 per day, 5730 per month): "))

url="https://api.opap.gr/draws/v3.0/1100/draw-date/" + date + "/" + date
req = requests.get(url)
data = req.json() # DICTIONARY!

# Get the last game's id
drawid = data["content"][0]["drawId"]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Starting Time =", current_time)

num = [] 
for i in range(80):
    num.append(0)

for i in range(drawid + 1 - num_games, drawid + 1):
    game_add = "https://api.opap.gr/draws/v3.0/1100/" + str(i)
    game = requests.get(game_add).json()
    for win in game["winningNumbers"]["list"]:
        num[win - 1] += 1


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Finishing Time =", current_time)

max_num = 0
max_occ = 0
for i in range(80): 
    if num[i] > max_occ:
        max_num = i
        max_occ = num[i]
        
print("The most common number was", max_num, "with", max_occ, "occurences.")
