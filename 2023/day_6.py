import pandas as pd

# Input
input_6 = {
    "Race": [1,2,3,4],
    "Time": [44, 80, 65, 72],
    "Distance": [208,   1581,   1050,  1102]
    }

# Create DataFrame from Input
df = pd.DataFrame(input_6)

# Calculate distance travelled for given time held and maximum time allowed
def dist_traveled(time, max_time):
    return (max_time - time) * time

# Calculate number of ways held_time results in a longer distance than achieved by the other elves
def calc_wins(max_time, distance):
    ways_to_win = 0
    for held_time in range(1, max_time):
        if dist_traveled(held_time, max_time) > distance:
            ways_to_win += 1
        else:
            pass
    return ways_to_win

# Create a new column which adds the number of hold times that beat the elves
df["ways_to_win"] = [calc_wins(time, dist) for time, dist in zip(df["Time"], df["Distance"])]

# The product of ways_to_win, sum of all the values multiplied by eachother
solution_1 = df["ways_to_win"].prod()
print(solution_1)

# Add new information to dataframe, at the last position in the dataframe
df.loc[len(df.index)] = [5, 44806572, 208158110501102] 

# Calculate wins for the last position of the dataframe
last_race = calc_wins(df["Time"].iloc[-1], df["Distance"].iloc[-1])
print(last_race)
