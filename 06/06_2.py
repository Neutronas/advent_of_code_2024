#Definitely not an ideal solution, it could be futher optimized to put obstacles only in the path
#that guard is actually walking instead of iterating throughout the whole map. However, this works too with bad performance.

import copy

with open("test.txt", "r") as file:
    lines = file.readlines()

array_2d = []
start_position = None

# Loop through each line and populate the array
for row_index, line in enumerate(lines):
    row = list(line.strip())  # Convert line into a list of characters (strip removes newline)
    array_2d.append(row)

    if "^" in row:
        col_index = row.index("^")
        start_position = (row_index, col_index)



unique_coordinates = set()
unique_coordinates.add(start_position) 

out_of_boundaries = False
current_coordinates = start_position
# 1 - top
# 2 - right
# 3 - down
# 4 - left
direction = 1

def change_direction(current_direction):
    if(current_direction == 4):
        current_direction = 1
    else:
        current_direction += 1
    return current_direction

found_cycle = False
visited_coords = []

def take_next_step():
    global direction
    global current_coordinates
    global out_of_boundaries
    global visited_coords
    global found_cycle

    match direction:
        case 1:
            next_step = (current_coordinates[0]-1, current_coordinates[1])
        case 2:
            next_step = (current_coordinates[0], current_coordinates[1]+1)
        case 3:
            next_step = (current_coordinates[0]+1, current_coordinates[1])
        case 4:
            next_step = (current_coordinates[0], current_coordinates[1]-1)
    if (next_step[0] == len(array_2d) or next_step[1] == len(array_2d[0]) or next_step[0]==-1 or next_step[1]==-1):
        out_of_boundaries = True
        return False
    if (array_2d[next_step[0]][next_step[1]] == '#'):
        direction = change_direction(direction)
    else:
        current_coordinates = next_step
        if [current_coordinates, direction] in visited_coords:
            found_cycle = True
        visited_coords.append([current_coordinates, direction])
        unique_coordinates.add(current_coordinates) 

sum = 0
etalon = copy.deepcopy(array_2d)
for i in range(0, len(array_2d)):
    for j in range(0, len(array_2d[0])):
        print(f'Pakeitimas ivyko {i} {j}')
        direction = 1
        array_2d = copy.deepcopy(etalon)
        current_coordinates = start_position
        out_of_boundaries = False
        found_cycle = False
        unique_coordinates = set()
        visited_coords = []
        if (not current_coordinates == (i, j)):
            array_2d[i][j] = '#'
        while(not out_of_boundaries):
            take_next_step()
            if found_cycle:
                sum += 1
                break

print(sum)

    