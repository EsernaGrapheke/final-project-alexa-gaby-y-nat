start algorythm 

def checkIfNextToSolution (matrix, ycoordinate, xcoordinate)
"""

Check if the current position is next to the solution
   :param matrix: any 2D matrix of any size
   :param xcoordinate: the x coordinate of the current position
   :param ycoordinate: the y coordinate of the current position
   :return: True if the current position is next to the solution, false otherwise
   """
   
   if matrix [xcoordinate][ycoordinate - 1] == 'S' or /
            matriz[xcoordinate-1][ycoordinate] == 'S' or /
            matriz[xcoordinate][ycoordinate + 1] == 'S' or /
            matrizxcoordinate + 1][ycoordinate] == 'S'
        return true
    else:
        return false
        
        
lab = [['x', 'x', 'x', 'x', 'x']
             ['x', ' ', ' ', ' ', 'S', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', ' ', ' ', 'x'],
             ['x', ' ', 'x', ' ', 'x', 'x'],
             ['x', ' ', ' ', 'E', ' ', 'x'], 
             ['x', 'x', 'x', 'x', 'x', 'x']]
             
             
PathLeft = false
PathRight = false
PathUpwards = false
PathDownards = false 

numberOfpaths = 0

row = 0
while row < len(lab): 
    column = 0 
    while column < len(lab[0]):
        if lab[row][column] == 'E'
            entranceRow = row
            entranceColumn = column
        column + = 1
    row + = 1
    
    currentLocationx = entranceColumn
    currentLocationy = entranceRow
    
    
while checkIfNextToSolution (lab, currentLocationx, currentLocationy) is false:
    if lab [currentLocationy][currentLocationx - 1] == " ":
        PathLeft = true
        numberOfpaths + = 1
    if lab [currentLocationy][currentLocationx + 1] == " ":
        PathRight = true
        numberOfpaths + = 1 
    if lab [currentLocationy - 1][currentLocationy] == " ":
        PathUpwards = true
        numberOfpaths + = 1 
    if lab [currentLocationy + 1][currentLocationx] == " ":
        PathDownards = true
        numberOfpaths + = 1 
    if PathLeft is true:
       lab [currentLocationy][currentLocationx - 1] = "." :
       currentLocationx = - 1 
    if PathRight is true:
       lab [currentLocationy][currentLocationx + 1] = ".": 
       currentLocationx + = 1 
    if PathUpwards is true:
       lab [currentLocationy - 1][currentLocationx] = ".":
       currentLocationy - = 1 
    if PathDownards is true: 
       lab [currentLocationy + 1][currentLocationx] = ".":
       currentLocationy + = 1 
       
    if numberOfpaths > 1:
        checkPointX = entranceColumn
        checkPointY = entranceRow
        
if checkIfNextToSolution (lab, currentLocationx, currentLocationy) is true:
    print ("you have arrived to the finish line correctly")
    print ("It took" numberOfpaths, "steps to arrive the finish line")
    
    def drawMatriz (matriz):
        for row in matriz:
            for column in row: 
                print (column,end = '')
            print ()
            
    
    def drawMatriz (matriz):
        for column in row: 
            print (row, end = '')
        print ()
            
end algorythm