file_path = "test.txt"

data = []

with open(file_path, 'r') as file:
    for line in file:
        row = [int(num) for num in line.strip().split()]
        data.append(row)

def check_sequence(arr):
    increasing = True
    decreasing = True
    
    for i in range(1, len(arr)):
        step = arr[i] - arr[i - 1]
        
        if abs(step) < 1 or abs(step) > 3:
            return False
        
        if step <= 0:
            increasing = False 
        if step >= 0:
            decreasing = False 

    return increasing or decreasing

results_array = []
unsafe_array = []

for row in data:
    if(check_sequence(row)):
        results_array.append(True)
    else:
        unsafe_array.append(row)

for unsafe in unsafe_array:
    found = False
    print(unsafe)
    for i in range(len(unsafe)):
        new_array = unsafe[:i] + unsafe[i+1:]  # Create a new array without the i-th element
        if(check_sequence(new_array)):
            found = True
            results_array.append(True)
            break


sum = 0
for result in results_array:
    if (result):
        sum += 1

print(sum)


