with open("data.txt", "r") as file:
    content = [list(line.rstrip('\n')) for line in file]

def checkA (x, y):
        #boundary check
        if (x == 0 or x == len(content)-1):
            return False
        if (y == 0 or y == len(content[x])-1):
            return False
        #MASMAS
        if (content[x-1][y-1] == 'M' and content[x+1][y+1] == 'S' and content[x-1][y+1] == 'M' and content[x+1][y-1] == 'S'):
             return True
        #MASSAM
        if (content[x-1][y-1] == 'M' and content[x+1][y+1] == 'S' and content[x-1][y+1] == 'S' and content[x+1][y-1] == 'M'):
             return True
        #SAMMAS
        if (content[x-1][y-1] == 'S' and content[x+1][y+1] == 'M' and content[x-1][y+1] == 'M' and content[x+1][y-1] == 'S'):
             return True
        #SAMSAM
        if (content[x-1][y-1] == 'S' and content[x+1][y+1] == 'M' and content[x-1][y+1] == 'S' and content[x+1][y-1] == 'M'):
             return True
        return False
 
    
sum = 0
for i, row in enumerate(content):
    for j, letter in enumerate(row):
        if (letter == 'A'):
            if(checkA(i, j)):
                 sum+=1
print(sum)

