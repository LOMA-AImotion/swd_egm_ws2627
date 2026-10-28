budget = int(input("Budget =?"))
used_budget = 0

# keep on adding square numbers as long as we have a budget
highest_so_far = 0
next_candidate = 1

while next_candidate**2 <= budget:
    # decrease the budget and store what we already have
    square_number = next_candidate * next_candidate
    budget = budget - square_number
    used_budget = used_budget + square_number
    next_candidate = next_candidate + 1

# print the highest number 
print(f"The highest number I could fit is: {next_candidate - 1}")

# print the used budget
print(f"The budget we used is: {used_budget}")