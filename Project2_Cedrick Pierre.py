# Project2
# COMP 151 Project 2 Platform Adventure Game

print("===== PLATFORM ADVENTURE =====")

#1: Create the Adventure
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

for i in range(len(levels)):
    print(f"Level {levels[i]}")
    print(f"Coins: {coins[i]}")
    print(f"Enemies: {enemies[i]}")
    print(f"Power-Up: {power_ups[i]}")

# Step 2 Player Information
player_name = "Hero"
lives = 3
score = 0
total_coins = 0

print("===== PLAYER INFORMATION =====")
print(f"Player: {player_name}")
print(f"Lives: {lives}")
print(f"Score: {score}")
print(f"Total Coins: {total_coins}")

# Step 3 Level Scores
level_scores = []

for i in range(len(levels)):
    level_score = coins[i] * 10 - enemies[i] * 5

    if power_ups[i] == "Star":
        level_score = level_score + 25

    level_scores.append(level_score)

print("===== LEVEL SCORES =====")
for i in range(len(levels)):
    print(f"Level {levels[i]} Score: {level_scores[i]}")

# Step 4 Adventure Actions
actions = [0, 1, 0, 2, 1]
action_results = []

print("===== ADVENTURE ACTIONS =====")

for i in range(len(actions)):
    if actions[i] == 0:
        action = "Collect Coins"
    elif actions[i] == 1:
        action = "Fight Enemies"
    else:
        action = "Use Power-Up"

    action_results.append(action)
    print(f"Level {levels[i]}: {action}")

# Step 5 Lives
life_history = []

for i in range(len(levels)):
    if enemies[i] >= 4 and power_ups[i] != "Star":
        lives = lives - 1

    life_history.append(lives)

print("===== LIFE HISTORY =====")
for i in range(len(levels)):
    print(f"After Level {levels[i]}: {life_history[i]} lives")

# Step 6 Coins
total_coins = sum(coins)
bonus_coin_levels = [coin for coin in coins if coin >= 7]

print("===== COIN COLLECTION =====")
print(f"Coins collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

# Step 7 Power-Up Inventory
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]

print("===== POWER-UP INVENTORY =====")
print(f"Starting Inventory: {inventory}")
print(f"Used Power-Ups: {used_powerups}")

for powerup in used_powerups:
    if powerup in inventory:
        inventory.pop(inventory.index(powerup))

print(f"Remaining Inventory: {inventory}")

# Step 8 Level Analysis
total_enemies = sum(enemies)
most_coins = max(coins)
fewest_coins = min(coins)
average_coins = total_coins / len(coins)
most_enemies = max(enemies)

print("===== LEVEL ANALYSIS =====")
print(f"Total Coins: {total_coins}")
print(f"Most Coins in One Level: {most_coins}")
print(f"Fewest Coins in One Level: {fewest_coins}")
print(f"Average Coins per Level: {average_coins}")
print(f"Total Enemies: {total_enemies}")
print(f"Most Enemies in One Level: {most_enemies}")

# Step 9 High Scores
high_scores = [level_score for level_score in level_scores
               if level_score >= 50]

print("===== HIGH SCORES =====")
print(f"Scores of 50 or Higher: {high_scores}")

# Step 10 Score History
score_history = []
score = 0

for i in range(len(levels)):
    score = score + level_scores[i]
    score_history.append(score)

print("===== SCORE HISTORY =====")
for i in range(len(levels)):
    print(f"After Level {levels[i]}: {score_history[i]}")

print(f"First Two Scores: {score_history[:2]}")
print(f"Last Two Scores: {score_history[-2:]}")

# Step 11 Final Status
print("===== FINAL STATUS =====")

if lives == 0:
    status = "Game Over"
elif score >= 250:
    status = "Adventure Champion"
elif score >= 150:
    status = "Great Adventure"
else:
    status = "Keep Practicing"

print(status)

print("===== ADVENTURE RANKING =====")
print(f"Final Score: {score}")
print(f"Final Lives: {lives}")

if score >= 300:
    rank = "Legend"
elif score >= 250:
    rank = "Champion"
elif score >= 150:
    rank = "Adventurer"
else:
    rank = "Beginner"

print(f"Rank: {rank}")



