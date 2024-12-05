tuples_list = []
updates = []
in_second_part = False 
with open('data.txt', 'r') as file:
    for line in file:
        line = line.strip() 
        if not line: 
            in_second_part = True
            continue

        if not in_second_part:
            left, right = map(int, line.split('|'))
            tuples_list.append((left, right))
        else:
            row = list(map(int, line.split(',')))
            updates.append(row)

correct_list = []
for row in updates:
    correct = True
    for i in range(1, len(row)):  
        for tuple in tuples_list:
            if (row[i] == tuple[1]):
                for z in range(i, len(row)):
                    if (tuple[0] == row[z]):
                        correct = False

    for i in range(0, i):  
        for tuple in tuples_list:
            if (row[i] == tuple[0]):
                for z in range(0, i):
                    if (tuple[1] == row[z]):
                        correct = False
    if (correct):
        correct_list.append(row)

sum = 0
for list in correct_list:
    sum += list[len(list)//2]

print(sum)

