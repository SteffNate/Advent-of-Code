import pandas as pd

df = pd.read_table("input_1.txt", delimiter="\t", header = None, names = ["instructions"])

df["numbers"] = [[i for i in instruction if i.isdigit() == True] for instruction in df["instructions"]]
df["numbers_2"] = [i[0]+i[-1] for i in df["numbers"]]

# Løsning
sum(df["numbers_2"].astype("int64"))

# Oppgave 2

list_char = ["one", "two","three", "four", "five", "six", "seven", "eight", "nine"]
list_num = ["o1e","t2o","thr3e","fo4r","fi5e","s6x","sev7n","eig8t","ni9e"]

# Dictionary konverterer fra 
chartonum = dict(zip(list_char, list_num))

df["instructions_fixed"] = df["instructions"].replace(chartonum, regex=True)

df["numbers_f"] = [[i for i in instruction if i.isdigit() == True] for instruction in df["instructions_fixed"]]
df["numbers_2_f"] = [i[0]+i[-1] for i in df["numbers_f"]]

# Løsning 2
sum(df["numbers_2_f"].astype("int64"))