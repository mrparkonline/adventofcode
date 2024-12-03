# Advent of Code 2024
# Day 2

''' Puzzle 2A Rules:
A report is safe if:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
'''

# helper function
def validate(report):
    safe = True
    increasing = True
    for i in range(1, len(report)):
        diff = abs(report[i-1] - report[i])
        if diff > 3 or diff < 1 :
            return False
        else:
            if i == 1:
                if report[i-1] > report[i]:
                    increasing = False
            else:
                if increasing and report[i-1] > report[i]:
                    return False
                elif not increasing and report[i-1] < report[i]:
                    return False
    # end of for
    return True
# end of validate()

clean_data = []
safe_reports = 0

# File IO
with open("./d1p2.txt", "r") as data_file:
    raw_data = data_file.readlines()
    for line in raw_data:
        line = line.replace("\n", "")
        data = line.split(" ")
        data = map(int, data)
        clean_data.append(list(data))
# END OF FILE IO

for report in clean_data:
    if validate(report):
        safe_reports += 1

print(f"Number of safe reports: {safe_reports}") # Answer = 356

# Puzzle 2B:
# We are allowed to move one single value to make it safe
# Brute Force Removal of values; if one of them removed
# causes a valid report then increase our counter
safe2 = 0
for report in clean_data:
    if validate(report):
        safe2 += 1
    else:
        for i in range(len(report)):
            test = report.copy()
            test.pop(i)
            if validate(test):
                safe2 += 1
                break
        
# end of outer for
print(f"Number of safe reports with dampeners: {safe2}")
