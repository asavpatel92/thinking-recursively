
#===============================================================================
# constants for creating maze
#===============================================================================
WALL = "#"
SPACE = " "
FINISH = "F"
PATH = "x"

#===============================================================================
# possible directions for the player to move. i.e four directions and if nothing works then failed
#===============================================================================
directions = ["North", "East", "South", "West", "Failed"]

#===============================================================================
# function to iterate through list of directions
#===============================================================================
def next(current, list):
    current_index = list.index(current)
    if current_index != len(list) - 1:
        return list[current_index + 1]
    
#===============================================================================
# array to generate maze
#===============================================================================
def generate_maze():
    maze = [[WALL, WALL,  WALL,  WALL,  WALL,   WALL,   WALL],
            [WALL, SPACE, WALL,  SPACE, SPACE,  SPACE,  WALL],
            [WALL, SPACE, WALL,  SPACE, WALL,   SPACE,  WALL],
            [WALL, SPACE, SPACE, SPACE, WALL,   SPACE,  WALL],
            [WALL, SPACE, WALL,  SPACE, WALL,   WALL,   WALL],
            [WALL, SPACE, WALL,  SPACE, SPACE,  FINISH, WALL],
            [WALL, WALL,  WALL,  WALL,  WALL,   WALL,   WALL]]
    return maze

def print_maze(maze):
    for r in range(len(maze)):
        for c in range(len(maze)):
            print "| %c " % (maze[r][c]),
        print ""
        
def find_path(maze, x, y):
    #===========================================================================
    # this is the base case. if player is on FINISH position then return true.
    #===========================================================================
    if maze[x][y] == FINISH:
        return True
    #===========================================================================
    # if player runs into WALL or PATH which is already discovered then return false.
    #===========================================================================
    if maze[x][y] == WALL or maze[x][y] == PATH: 
        return False
    if maze[x][y] == SPACE:
        maze[x][y] = PATH
        #=======================================================================
        #=======================================================================
        # # always pick and start with that direction here i have taken "NORTH"
        #=======================================================================
        #=======================================================================
        dir = "North"
        found = False
        #=======================================================================
        # after starting with NORTH explore all different four directions and go further in those direction. 
        # so each call to find_path will try to discover it's own path and move further by it self
        #=======================================================================
        while (not found and  dir != "Failed"):
            if dir == "North":
                found = find_path(maze, x-1, y)
            if dir == "East":
                found = find_path(maze, x, y+1)
            if dir == "South":
                found = find_path(maze, x+1, y)
            if dir == "West":
                found =  find_path(maze, x, y-1)
            dir = next(dir, directions)
        #=======================================================================
        # if no path is found in any direction then backtrack and start again from the previous point and clear the path
        #=======================================================================
        if not found:
            maze[x][y] = SPACE
            return False
        else:
            return True

def main():
    maze = generate_maze()
    print_maze(maze)
    find_path(maze, 3, 3)
    print "Solved path is :"
    print_maze(maze)

if __name__ == '__main__':
    main()