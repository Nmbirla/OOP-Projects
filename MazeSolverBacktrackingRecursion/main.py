# Material reference used:
# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
# https://www.codesdope.com/blog/article/backtracking-to-solve-a-rat-in-a-maze-c-java-pytho/
# https://runestone.academy/runestone/books/published/pythonds/Recursion/ExploringaMaze.html

class Maze:
    def __init__(self, mazefile):
        """Reads .txt file and locates starting position on Maze"""
        r_maze = 0
        col_maze = 0
        self.mazelist = []  # Define empty list
        mazefile = open(mazefile, 'r')  # Open Maze file
        # r_maze = 0
        for line in mazefile:
            r_list = []  # Define empty row list
            col = 0
            for pos in line[:-1]:
                r_list.append(pos)
                if pos == 'S':  # Loop to locate S in Maze
                    self.startRow = r_maze
                    self.startCol = col
                col = col + 1
            r_maze = r_maze + 1
            self.mazelist.append(r_list)
            col_maze = len(r_list)

        self.rowsInMaze = r_maze
        self.columnsInMaze = col_maze

    def update_position(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze - 1 or
                col == 0 or
                col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]

    # def resetMaze(self,maze_p):
    #     self.mazelist=maze_p


def print_maze(maze_l):
    for line in range(len(maze_l)):
        print(maze_l[line])
    print("\n")

def next_position(maze, start_row, start_column):
    found = 0
    path = 0
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == '1':  # OBSTACLE
        return False

    if maze[start_row][start_column] == 'v':  # VISITED
        return False

    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, 'p')  # PART_OF_PATH
        print_maze(maze.mazelist)
        print('Path found')
        print('Path length = ', path)
        return True
    maze.update_position(start_row, start_column, 'v')

    if 1 - found:
        if next_position(maze, start_row, start_column + 1):
            found = 1
            maze.update_position(start_row, start_column, 'p')

        elif next_position(maze, start_row + 1, start_column):
            found = 1
            maze.update_position(start_row, start_column, 'p')

        elif next_position(maze, start_row, start_column - 1):
            found = 1
            maze.update_position(start_row, start_column, 'p')

        elif next_position(maze, start_row - 1, start_column):
            found = 1
            maze.update_position(start_row, start_column, 'p')
        else:
            maze.update_position(start_row, start_column, 'd')  # DEAD_END
        print_maze(maze.mazelist)
        return found

myMaze = Maze('maze.txt')

myMaze.update_position(myMaze.startRow, myMaze.startCol)
next_position(myMaze, myMaze.startRow, myMaze.startCol)
