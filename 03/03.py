import re

with open("test.txt", "r") as file:
    content = file.read()

# Define the regular expression to match mul(X, Y)
# X and Y are 1 to 3 digits (\d{1,3})
pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"

# Use re.findall to extract all matches
matches = re.findall(pattern, content)

# Convert matches into a list of tuples (X, Y) with integer values
results = [(int(x), int(y)) for x, y in matches]

total_sum = sum(x * y for x, y in results)

# Print the results
print(total_sum)