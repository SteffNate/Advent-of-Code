import pandas as pd
df = pd.read_table("input_7.txt", sep=" ", names=["hand", "bet"])

# Part 1
# Find hand strength
def get_hand_strength(hand):
    unique_cards = len(set(hand))

    if unique_cards == 1:
        return "Five of a kind"
    if unique_cards == 5:
        return "High card"
    if unique_cards == 4:
        return "One pair"
    if unique_cards == 2 and ((hand.count(hand[0]) == 4) or (hand.count(hand[1]) == 4)):
        return "Four of a kind" 
    if unique_cards == 2:
        return "Full house"    
    if unique_cards == 3 and ((hand.count(hand[0]) == 2) or ( hand.count(hand[1]) == 2)):
        return "Two pairs"
    if unique_cards == 3:
         return "Three of a kind"

    else:
        return "Wrong"
# Get values for cards in hand
  def get_hand_values(hand):
    card_values = []

    for card in hand:
        card_values.append(card_value[card])
    return card_values

# Dict for card-value conversion
card_value = {
    "A": 14,
    "K": 13, 
    "Q": 12, 
    "J": 11, 
    "T": 10, 
    "9": 9, 
    "8": 8, 
    "7": 7, 
    "6": 6, 
    "5": 5, 
    "4": 4, 
    "3": 3, 
    "2": 2, 
}
# Dict for hand-strength conversion
sort_strong_to_weak = {
    "Five of a kind" : 6,
    "Four of a kind" : 5,
    "Full house" : 4,
    "Three of a kind" : 3,
    "Two pairs" : 2,
    "One pair" : 1,
    "High card" : 0
}
# Get hand strength for data
df["rank"] = df["hand"].apply(get_hand_strength)

# Get number for rank and sorting
df["rank_value"] = df["rank"].map(sort_strong_to_weak)

# Get the value corresponding to each hand
df["card_values"] = df["hand"].apply(get_hand_values)

# Explode each card into columns for sorting
df[["card_1", "card_2", "card_3", "card_4", "card_5"]] = pd.DataFrame(df["card_values"].tolist(), index= df.index)

# Sort data by each hand and card 1 to 5, in ascending order. Reset index so that new positions in list are index
sorted_hands = df.sort_values(by=["rank_value", "card_1", "card_2", "card_3", "card_4", "card_5"], ascending=True).reset_index()

# Get the sum of each hand by multiplying the bet with index
sorted_hands["sum_points"] = sorted_hands["bet"] * (sorted_hands.index +1)

# Solution 1
print(sorted_hands["sum_points"].sum())
