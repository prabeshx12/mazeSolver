import turtle
import time
from collections import deque
from tkinter import messagebox


class Maze(turtle.Turtle):  # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("brown")
        self.penup()
        self.speed(0)


class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)



class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


class White(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


grids = [
    [
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",  # simple maze
        "e                                                 +",
        "+                                                 +",
        "+                                                 +",
        "+                                                 +",
        "+                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++ +",
        "+                                                 +",
        "+ +++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++ +",
        "+                                                 +",
        "+ +++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++ +",
        "+                                                 +",
        "+ +++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++ +",
        "+                                                 +",
        "+ +++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++ +",
        "s                                                 +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",
        ],
    
    [
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",  # medium maze
        "+               +                                 s",
        "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
        "+           +                 +               ++  +",
        "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
        "+  +     +  +           +  +                 +++  +",
        "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
        "+  +  +  +  +  +  +        +  +  +        +       +",
        "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
        "+  +     +  +          +   +           +  +  ++  ++",
        "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
        "+     +  +     +              +              ++   +",
        "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
        "+  +  +                    +     +     +  +  +++  +",
        "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
        "+  +  +     +     +     +  +  +     +     +  ++  ++",
        "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
        "+                       +  +  +              ++  ++",
        "+ ++++++             +  +  +  +  +++        +++  ++",
        "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
        "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
        "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
        "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
        "+      ++ +++++++ +++     ++          ++    +++++++",
        "+++++++++++++++++e+++++++++++++++++++++++++++++++++",
            ],


    [
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",  # hard maze
        "s  +                      +      ++            ++ +",
        "+  ++++   +++++++   +++++ ++++   +   +++++        +",
        "+          +      ++++    +         + +   +    ++ +",
        "+  ++++ +++++ ++++++++ ++++++  +++++++++++++ ++++ +",
        "+  +   +     + + +       +   + +     +       +  + +",
        "+  ++++ +++++ +  +  +++ + + +  ++++ ++ +++++++ +  +",
        "+       +    +    +  +   + + +  +  +   +          +",
        "+  ++++ +++++ ++++  +++++++++ +  +++ ++++++ ++++ ++",
        "+     +    +      +        +        +   +    + +  e",
        "+++++ + ++++++++ + +++++++++ ++++++ ++++ + ++++   +",
        "+   + +         + +          + +       + +      + +",
        "+++++ + ++++++ +++ + +++++++ + ++++ +++ ++ +++++ ++",
        "+     +       + +            ++          +     +  +",
        "+ ++++++++++ ++++++++++ ++ +++++++ ++++ + ++++ ++++",
        "+          + +    +       +     + +   + +        ++",
        "++++++ ++++++++++ + ++++ +++++++++ + ++  ++  ++++ +",
        "+       +       + +    + +     +   + + + + +    + +",
        "+  ++++++ ++++  ++++ + ++ ++ + + + + +++ + +++ + ++",
        "+  +  +   +   + +  +  +   +     + +   +   +     + +",
        "+  +  +++  + +   ++     + + + + + +++    +++ +  + +",
        "+         + + + +   ++ +    +  ++  +++++        + +",
        "+  +++++++++ ++  + +++++ ++    + ++++ ++++ ++++++++",
        "+  +   +    +             + +  +                  +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",

        ],

    [
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",  # impossible maze
        "s  +                      +      ++            ++ +",
        "+  ++++   +++++++   +++++ ++++   +   +++++        +",
        "+          +      ++++    +         + +   +    ++ +",
        "+  ++++ +++++ ++++++++ ++++++  +++++++++++++ ++++ +",
        "+  +   +     + + +       +   + +e"
        "    +       +  + +",
        "+  ++++ +++++ +  +  +++ + + +  ++++ ++ +++++++ +  +",
        "+       +    +    +  +   + + +  +  +   +          +",
        "+  ++++ +++++ ++++  +++++++++ +  +++ ++++++ ++++ ++",
        "+     +    +      +        +        +   +    + +  +",
        "+++++ + ++++++++ + +++++++++ ++++++ ++++ + ++++   +",
        "+   + +         + +          + +       + +      + +",
        "+++++ + ++++++ +++ + +++++++ + ++++ +++ ++ +++++ ++",
        "+     +       + +            ++          +     +  +",
        "+ ++++++++++ ++++++++++ ++ +++++++ ++++ + ++++ ++++",
        "+          + +    +       +     + +   + +        ++",
        "++++++ ++++++++++ + ++++ +++++++++ + ++  ++  ++++ +",
        "+       +       + +    + +     +   + + + + +    + +",
        "+  ++++++ ++++  ++++ + ++ ++ + + + + +++ + +++ + ++",
        "+  +  +   +   + +  +  +   +     + +   +   +     + +",
        "+  +  +++  + +   ++     + + + + + +++    +++ +  + +",
        "+         + + + +   ++ +    +  ++  +++++        + +",
        "+  +++++++++ ++  + +++++ ++    + ++++ ++++ ++++++++",
        "+  +   +    +             + +  +                  +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++++",
        ]

]


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -600 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.goto(screen_x, screen_y)
                green.stamp()
                end_x, end_y = screen_x, screen_y

            if character == "s":
                start_x, start_y = screen_x, screen_y
                yellow.goto(screen_x, screen_y)


def endProgram():
    window.exitonclick()


def free():
    window.bye()


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:  # exit while loop when frontier queue equals zero
        try:
            time.sleep(0.02)
            x, y = frontier.popleft()  # pop next entry in the frontier queue an assign to x and y location

            if (x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
                cell = (x - 24, y)
                solution[cell] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
                # blue.goto(cell)        # identify frontier cells
                # blue.stamp()
                frontier.append(cell)  # add cell to frontier list
                visited.add((x - 24, y))  # add cell to visited list

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
                cell = (x, y - 24)
                solution[cell] = x, y
                # blue.goto(cell)
                # blue.stamp()
                frontier.append(cell)
                visited.add((x, y - 24))

            if (x + 24, y) in path and (x + 24, y) not in visited:  # check the cell on the  right
                cell = (x + 24, y)
                solution[cell] = x, y
                # blue.goto(cell)
                # blue.stamp()
                frontier.append(cell)
                visited.add((x + 24, y))

            if (x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
                cell = (x, y + 24)
                solution[cell] = x, y
                # blue.goto(cell)
                # blue.stamp()
                frontier.append(cell)
                visited.add((x, y + 24))
            green.goto(x, y)
            green.stamp()
        except:
            messagebox.showerror("Error", "Path couldn't ne searched!!")


def backTrack(x, y):
    try:
        white.goto(x, y)
        white.stamp()
        while (x, y) != (start_x, start_y):  # stop loop when current cells == start cell
            time.sleep(0.02)
            white.goto(solution[x, y])  # move the yellow sprite to the key value of solution ()
            white.stamp()
            x, y = solution[x, y]  # "key value" now becomes the new key
        messagebox.showinfo("Success", "Congratulations! Path is Successfully found!!")
    except:
        messagebox.showerror("Error", "Sorry!! Path not found!!")


def setup_screen():
    global window
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Maze Solving")
    window.setup(1300, 700)


def start_solving(value):
    setup_screen()
    global maze, yellow, blue, green, white, walls, path, visited, frontier, solution
    maze = Maze()
    yellow = Yellow()
    blue = Blue()
    green = Green()
    white = White()

    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}

    setup_maze(grids[value])
    search(start_x, start_y)
    backTrack(end_x, end_y)
    endProgram()

