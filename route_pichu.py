#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0)]
        closed = []
        closed_only_steps=[]
        only_steps = [(pichu_loc)]
        succ_A = []
        succ_B = []
        final_path = []

        while True:
                if fringe == []:
                    return -1
                (curr_move, curr_dist)=fringe.pop()
                only_steps.pop()
                closed.append((curr_move, curr_dist))
                closed_only_steps.append(curr_move)
                


                if house_map[curr_move[0]][curr_move[1]] == "@":
                        
                        state = curr_move
                        final_path.append(state)
                        while True:
                                if state not in succ_B:
                                        break
                                index = succ_B.index(state)
                                final_path.append(succ_A[index])
                                state = succ_A[index]

                        final_path_str = ""
                        final_path.reverse()
                        for i in range(len(final_path)-1):
                                if (final_path[i+1][0]+1,final_path[i+1][1]) == (final_path[i][0],final_path[i][1]):
                                        final_path_str += "U"
                                elif (final_path[i+1][0]-1,final_path[i+1][1]) == (final_path[i][0],final_path[i][1]):
                                        final_path_str += "D"
                                elif (final_path[i+1][0],final_path[i+1][1]+1) == (final_path[i][0],final_path[i][1]):
                                        final_path_str += "L"
                                elif (final_path[i+1][0],final_path[i+1][1]-1) == (final_path[i][0],final_path[i][1]):
                                        final_path_str += "R"
                                else:
                                        print("SOMETHING IS WRONG")         
                                

                        return (curr_dist, final_path_str)
                

                #for every SUCC(s):
                for move in moves(house_map, *curr_move):
                        succ_A.append(curr_move)
                        succ_B.append(move)
                        
                        if move in closed_only_steps:
                                continue
                        if move in only_steps:
                                #print(fringe[only_steps.index(move)][1],curr_dist)
                                if fringe[only_steps.index(move)][1] >= curr_dist:
                                        
                                        fringe.remove(fringe[only_steps.index(move)])
                                        only_steps.remove(move)

                        if move not in only_steps:
                                fringe.append((move, curr_dist + 1))
                                only_steps.append(move)
                                
                                
                




                        # if house_map[move[0]][move[1]]=="@":
                        #         return (7, 'DDDDDDD')  # return a dummy answer
                        # else:
                        #         fringe.append((move, curr_dist + 1))

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])