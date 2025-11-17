with open("inputs/everybody_codes_e2025_q05_p1.txt", "r") as f:
    id, numbers = f.read().split(":")
    sword_parts = [int(i) for i in numbers.split(",")]


sword = [None for i in range(0, len(sword_parts))]

print(sword_parts)

n = len(sword_parts)
for i in sword_parts:
    placed = False
    sword_stage = 1

    while not placed and 0 <= sword_stage < n:
        if sword[sword_stage] is None:
            sword[sword_stage] = i
            placed = True
        elif i > sword[sword_stage]:
            if sword[sword_stage - 1] is None:
                sword[sword_stage - 1] = i
                placed = True
        elif i < sword[sword_stage]:
            if sword[sword_stage + 1] is None:
                sword[sword_stage + 1] = i
                placed = True

        sword_stage += 3

print("".join([str(sword[i]) for i in range(1, len(sword), 3)]))

# Check all segments of the spine, starting from the top.
# If your number is less than the one on the spine segment and the left side of the segment is free - place it on the left.
# If your number is greater than the one on the spine segment and the right side of the segment is free - place it on the right.
# If no suitable place is found at any segment, create a new spine segment from your number and place it as the last one.
#
# 0,1,2,3,4,5,6
# v,m,h,v,m
