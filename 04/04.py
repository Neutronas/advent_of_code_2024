with open("data.txt", "r") as file:
    content = [list(line.rstrip('\n')) for line in file]

def checkTop (x, y):
    try: 
        if (content[x-1][y] == 'M'):
            if (content[x-2][y] == 'A'):
                if (content[x-3][y] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkTopLeft (x, y):
    try: 
        if (content[x-1][y-1] == 'M'):
            if (content[x-2][y-2] == 'A'):
                if (content[x-3][y-3] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkTopRight (x, y):
    try: 
        if (content[x-1][y+1] == 'M'):
            if (content[x-2][y+2] == 'A'):
                if (content[x-3][y+3] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkRight (x, y):
    try: 
        if (content[x][y+1] == 'M'):
            if (content[x][y+2] == 'A'):
                if (content[x][y+3] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkLeft(x, y):
    try: 
        if (content[x][y-1] == 'M'):
            if (content[x][y-2] == 'A'):
                if (content[x][y-3] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkBottom (x, y):
    try: 
        if (content[x+1][y] == 'M'):
            if (content[x+2][y] == 'A'):
                if (content[x+3][y] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkBottomLeft (x, y):
    try: 
        if (content[x+1][y-1] == 'M'):
            if (content[x+2][y-2] == 'A'):
                if (content[x+3][y-3] == 'S'):
                    return True
        return False
    except:
        return False
    
def checkBottomRight (x, y):
    try: 
        if (content[x+1][y+1] == 'M'):
            if (content[x+2][y+2] == 'A'):
                if (content[x+3][y+3] == 'S'):
                    return True
        return False
    except:
        return False
    
sum = 0
for i, row in enumerate(content):
    for j, letter in enumerate(row):
        if (letter == 'X'):
            if(checkTop(i, j) and i >= 3):
                sum+=1
            if(checkTopLeft(i, j) and i >= 3 and j-3 >= 0):
                sum+=1
            if(checkTopRight(i, j) and i >= 3 and j+3 < len(row)):
                sum+=1
            if(checkRight(i, j) and j+3 < len(row)):
                sum+=1
            if(checkLeft(i, j) and j-3 >= 0):
                sum+=1
            if(checkBottom(i, j) and i+3 < len(content)):
                sum+=1
            if(checkBottomRight(i, j) and i+3 < len(content) and j+3 < len(row)):
                sum+=1
            if(checkBottomLeft(i, j) and i+3 < len(content) and j-3 >= 0):
                sum+=1
print(sum)

