import os

# Set the directory path
dir = r'D:\My Documents\GitHub\basketball-and-data-science\content\data\nba-players'

# Initialize an empty list to store player files
player_files = []

# Iterate over each file in the directory and append the filename to the player_files list
for filename in os.listdir(dir):
    player_files.append(filename)

# Print the contents of the player_files list
print(player_files)
