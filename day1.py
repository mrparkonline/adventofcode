# Advent of Code 2024
# Day 1

''' Instructions for Puzzle 1:
Pair up the smallest number in the left list with the smallest number in the right list

then the second-smallest left number with the second-smallest right number, and so on

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances

For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
'''
# Variable Initializations
clean_data = []
left = []
right = []
total_distance = 0

# File IO reading the data of our puzzle input
with open("./d1p1a.txt", 'r') as data_file:
    raw_data = data_file.readlines()
    for line in raw_data:
        line = line.replace("\n", "")
        item = line.split("   ")

        left.append(int(item[0]))
        right.append(int(item[1]))
# END OF FILE IO

# Sort the both list
left.sort()
right.sort()

for i in range(len(left)):
    item1 = left[i]
    item2 = right[i]

    total_distance += abs(item1 - item2)

# PART 1 Output
print(f"total distance between the left list and the right list and their distance pairs: {total_distance}")
# PART 1 FINISHED

""" Part 2:

Output the similarity score:
- Each item in the left list is multiplied by their frequency in the right list
- Total up the left list's similarity score.
"""

similarity = 0

for item1 in left:
    item1_count = right.count(item1)

    similarity += (item1 * item1_count)

print(f"The similarity total score is: {similarity}")