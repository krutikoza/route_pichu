#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [NAME: Krutik Oza, USERNAME: KAOZA]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#

def check_row_column_diagonal(initial_house_map,occupied_space,i,j,row_occupied,column_occupied, wall_x, wall_y, comb_wall):
    row_column_sub =[]
    row_column_sum = []


    for num1, num2 in zip(row_occupied, column_occupied):
	    row_column_sub.append(num1 - num2)
        

    for num1, num2 in zip(row_occupied, column_occupied):
	    row_column_sum.append(num1 + num2)


    wall_row_column_sub =[]
    wall_row_column_sum = []
    

    
    for num1, num2 in zip(wall_x, wall_y):
	    wall_row_column_sub.append(num1 - num2)
        

    for num1, num2 in zip(wall_x, wall_y):
	    wall_row_column_sum.append(num1 + num2)

    # for num1, num2 in zip(wall_x, wall_y):
	#     wall_row_column_mul.append(num1 * num2)

    

    #Check condition if in diagonal(Top right to Bottem left)
    if (i+j in row_column_sum):
        index_occupied = row_column_sum.index(i+j)
        if (i+j in wall_row_column_sum):
            for p,q in zip(range(i,-1,-1),range(j,-1,-1)):
                if (initial_house_map[p][q] == 'X'):
                    break
                if (initial_house_map[p][q] == 'p'):
                    return False
        else:    
            return False

    #Check condition if in diagonal(Bottem left to Top right)
    if (i-j in row_column_sub):
        index_occupied = row_column_sub.index(i-j)
        if (i-j in wall_row_column_sub):
            for p,q in zip(range(i,-1,-1),range(j,-1,-1)):
                if (initial_house_map[p][q] == 'X'):
                    break
                elif (initial_house_map[p][q] == 'p'):
                    return False
        else:    
            return False
    
    #Check conditions for same row
    if (i in row_occupied):
        
        if (i in wall_x):
            #index_wall = wall_x.index(i)

            for p in range(j,-1,-1):
                if (initial_house_map[i][p] == 'X'):
                    break
                if (initial_house_map[i][p] == 'p'):
                    return False
        else:
            return False

    #check conditions for same column
    if (j in column_occupied):
        if (j in wall_y):

            for p in range(i,-1,-1):
                if (initial_house_map[p][j] == 'X'):
                    break
                if (initial_house_map[p][j] == 'p'):
                    return False
        else:
            return False




    # if (i+j in row_column_sum) or (i-j in row_column_sub) or (i in row_occupied) or (j in column_occupied):
    #     return False
    return True    


def solve(initial_house_map,k):
    # fringe = [initial_house_map]
    # while len(fringe) > 0:
    #     for new_house_map in ( fringe.pop() ):
    #         if is_goal(new_house_map,k):
    #             return(new_house_map,True)
    #         fringe.append(new_house_map)

    #counters for loop
    i_rows = 0
    j_columns = 0

    #store length of rows and columns
    len_rows = len(initial_house_map)-1
    len_columns = len(initial_house_map[0])-1


    #To store positions of wall
    wall_x = []
    wall_y = []
    comb_wall = []

    #Get the wall positions
    for i in range(len_rows+1):
        for j in range(len_columns+1):
            if initial_house_map[i][j] == 'X':
                comb_wall.append([i,j])
                wall_x.append(i)
                wall_y.append(j)

    #initializa variable to save positions of pichus in the map
    row_occupied = []
    column_occupied = []
    occupied_space = []

    #get the position of one pichu in the map
    pichu_loc=[(row_i,col_i) for col_i in range(len(initial_house_map[0])) for row_i in range(len(initial_house_map)) if initial_house_map[row_i][col_i]=="p"][0]

    #remove the first pichu from the map
    
    initial_house_map[pichu_loc[0]][pichu_loc[1]] = '.'



    #main loop
    while True:
        #print("i = ",i_rows, "j = ", j_columns)
        #no_inc = False
        if (initial_house_map[i_rows][j_columns] != 'X') and (initial_house_map[i_rows][j_columns] != '@') and (check_row_column_diagonal(initial_house_map,occupied_space,i_rows,j_columns, row_occupied, column_occupied,wall_x, wall_y,comb_wall) == True):
            initial_house_map[i_rows][j_columns] = 'p'
            #print('p')
            row_occupied.append(i_rows)
            column_occupied.append(j_columns)
            occupied_space.append([i_rows,j_columns])

            if len(occupied_space) == k:
                return (initial_house_map, True)
            
        
            # elif (j_columns == len_columns):
            #     i_rows=i_rows+1
            #     j_columns = -1
            

        # elif (j_columns == len_columns):
        #     while True:
        #         if i_rows == 0:
        #             return "No solution"
                
        #         #go to the previous row
        #         i_rows = i_rows-1
        #         #get the index of the 'p' we put previously
        #         j_columns = column_occupied[row_occupied.index(i_rows)]
                
        #         #remove stored index of 'p'
        #         row_occupied.remove(i_rows)
        #         column_occupied.remove(j_columns)
        #         #chenge 'p' back to '.'
        #         initial_house_map[i_rows][j_columns] = '.'


        #         if j_columns == len_columns:
        #             continue
        #         break



        if j_columns == len_columns:
            if i_rows == len_rows:
                #No increment=False
                if occupied_space == []:
                    return(initial_house_map,False)
                else:
                    
                    i_rows = row_occupied[-1]
                    j_columns = column_occupied[-1]
                    initial_house_map[i_rows][j_columns] = '.'
                    row_occupied.pop()
                    column_occupied.pop()
                    occupied_space.pop()
                    
                    if (j_columns == len_columns):
                        j_columns = -1
                        i_rows = i_rows + 1
            else:
                j_columns = -1
                i_rows = i_rows + 1
             
        j_columns=j_columns+1


# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")