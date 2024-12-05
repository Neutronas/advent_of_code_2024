import re

# Read the content of the test.txt file
with open("test.txt", "r") as file:
    content = file.read()

# Define the regular expressions
mul_pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"  # Matches valid mul(X, Y)
trigger_pattern = r"do\(\)|don't\(\)"           # Matches do() or don't()

# Split the input string into tokens based on triggers
tokens = re.split(trigger_pattern, content)
print(tokens)
# Find all triggers in the input string to determine their positions
triggers = re.findall(trigger_pattern, content)
print(triggers)


# Initialize inclusion state and results list
include = True
results = []

# Process tokens with respect to triggers
for i, token in enumerate(tokens):
    # Update inclusion state based on the trigger before this token
    if i > 0 and i - 1 < len(triggers):  # Ensure there's a corresponding trigger
        if triggers[i - 1] == "do()":
            include = True
        elif triggers[i - 1] == "don't()":
            include = False
    
    # Extract and process mul(X, Y) only if `include` is True
    if include:
        matches = re.findall(mul_pattern, token)
        results.extend((int(x), int(y)) for x, y in matches)

# Multiply the values inside each tuple and sum them up
total_sum = sum(x * y for x, y in results)

print(total_sum)
