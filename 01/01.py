file_path = "01.txt"

first_array = []
second_array = []

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        first_number = int(parts[0]) 
        second_number = int(parts[1]) 
        first_array.append(first_number)
        second_array.append(second_number)

sorted_numbers1 = sorted(first_array)
sorted_numbers2 = sorted(second_array)

sum = 0
for index, number in enumerate(sorted_numbers1):
    if (number > sorted_numbers2[index]):
        sum+= number-sorted_numbers2[index]
    else:
        sum+=sorted_numbers2[index]-number
print(sum)
