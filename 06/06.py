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

def take_next_step():
    global direction
    global current_coordinates
    global out_of_boundaries
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
        unique_coordinates.add(current_coordinates) 

while(not out_of_boundaries):
   take_next_step()

print(len(unique_coordinates))

    