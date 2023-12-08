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


# Part 2
# Switched the joker to value 1
new_card_value = {
    "A": 14,
    "K": 13, 
    "Q": 12, 
    "J": 1, 
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
# Get the new value of the hand
def get_new_hand_values(hand):
    card_values = []

    for card in hand:
        card_values.append(new_card_value[card])
    return card_values
    
# Create the best hand
def card_check_and_append(hand):
    while "J" in hand:
        hand.remove("J")
    
    new_card = check_for_largest_reps(hand)

    while len(hand) != 5:
        hand.append(new_card)
    
    return hand
    
# find the most repetitions in each hand, return max repetitions
def check_for_largest_reps(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1
    
    return max(card_counts, key=card_counts.get)

# Get the best hand, from different length of unique cards
def get_best_hand(hand):

    if "J" in hand:
        unique_cards = len(set(hand))
        temp_hand = list(hand)

        # Same card for all card, return all (all the JJJJJJJJJJJJs)
        if unique_cards == 1:
            return "".join(hand)
        
        # Two unique cards
        if unique_cards == 2:

            while "J" in temp_hand:
                temp_hand.remove("J")
            
            while len(temp_hand) != 5:
                temp_hand.append(temp_hand[0])

            return "".join(temp_hand)
        
        # Three unique cards
        if unique_cards == 3:
            best_hand = card_check_and_append(temp_hand)
            return "".join(best_hand)

        # Four unique cards
        if unique_cards == 4:
            best_hand = card_check_and_append(temp_hand)
            return "".join(best_hand)
        
        # Five unique cards
        else:
            best_hand = card_check_and_append(temp_hand)
            return "".join(best_hand)
    else:
        return hand   

# Create the new best hand from old hand
df["new_hand"] = df["hand"].apply(get_best_hand)
# Get the newly created hand strength
df["new_rank"] = df["new_hand"].map(get_hand_strength)
# Give the new rank a numeric value for easier sorting
df["new_rank_value"] = df["new_rank"].map(sort_strong_to_weak)
# Give the new cards new values for sorting
df["new_card_values"] = df["hand"].map(get_new_hand_values)
# Create a column for each card
df[["new_card_1", "new_card_2", "new_card_3", "new_card_4", "new_card_5"]] = pd.DataFrame(df["new_card_values"].tolist(), index= df.index)

# Sort values by rank then card 1 to 5, using new values
new_sorted_hands = df.sort_values(by=["new_rank_value", "new_card_1", "new_card_2", "new_card_3", "new_card_4", "new_card_5"], ascending=True).reset_index()

# Find sum for each new hand with index position
new_sorted_hands["sum_points"] = new_sorted_hands["bet"] * (new_sorted_hands.index +1)
# Solution 2
print(new_sorted_hands["sum_points"].sum())
