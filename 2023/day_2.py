import pandas as pd

data = pd.read_table("2.txt", names=["input"])

data[["game", "subsets"]] = data["input"].str.split(":", expand=True)

# Get game number
pattern = r'\b\d+\b'
data["game_nr"] = data["game"].str.findall(pattern)

data['game_nr'] = data['game_nr'].apply(lambda x: int(x[0]) if x else None)

# Seach patterns 
pattern_g = r'(\d+) green'
pattern_b = r'(\d+) blue'
pattern_r = r'(\d+) red'

# Find subsets of each color in
data["green"] = data["subsets"].str.findall(pattern_g)
data["blue"] = data["subsets"].str.findall(pattern_b)
data["red"] = data["subsets"].str.findall(pattern_r)

# Find largest instance of coloured cube in subset
data["max_g"] = data['green'].apply(lambda x: max(map(int, x)) if x else 0)
data["max_b"] = data['blue'].apply(lambda x: max(map(int, x)) if x else 0)
data["max_r"] = data['red'].apply(lambda x: max(map(int, x)) if x else 0)

# Set number of cubes
g = 13
b = 14
r = 12

# Filter possible games
possible_games = data.loc[(data["max_g"] <= g) & (data["max_b"] <= b) & (data["max_r"] <= r)]["game_nr"]

# Solution part 1
possible_games.sum()

# Solution part 2
data["power_of_games"] = data["max_g"] * data["max_b"] * data["max_r"]
data["power_of_games"].sum()
