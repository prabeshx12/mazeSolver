from tkinter import *
from PIL import Image, ImageTk
import new_maze_solver

root = Tk()
root.geometry('1000x800')
root.title("Maze Solver")
root.maxsize(height=800, width=1000)
root.minsize(height=800, width=1000)
root.config(bg="lightseagreen")


def solve_maze():
    value = int(r.get())
    new_maze_solver.start_solving(value)


def free_turtle():
    new_maze_solver.tur_reset()
    

r = IntVar()

# for background image
background_image = Image.open("images/background.png")
resized_image = background_image.resize((350, 400))
res_background_image = ImageTk.PhotoImage(resized_image)

title = Label(root, text="We present to you Maze Solver", font="TimesNewRoman, 20", bg="lightblue", height=2, width=50)
title.pack(pady=20)

image_frame = Frame(root)
image_frame.pack(pady=20)

image_maze = Label(image_frame, height=350, width=400, image=res_background_image)
image_maze.pack(pady=20)

select_level = Label(root, text="Please chose your maze difficulty level!!", font="TimesNewRoman, 18", bg="lightpink",
                     height=1, width=50)
select_level.pack(pady=20)

# background for radio buttons
background_radio = Frame(root, bg="lightseagreen")
background_radio.pack()

# radio easy
easy_radio = Radiobutton(background_radio, variable=r, value=0, text="EASY", font="TimesNewRoman, 15")
easy_radio.pack(padx=25, pady=10, side=LEFT)

# radio medium
medium_radio = Radiobutton(background_radio, variable=r, value=1, text="MEDIUM", font="TimesNewRoman, 15")
medium_radio.pack(padx=25, pady=10, side=LEFT)

# radio hard
hard_radio = Radiobutton(background_radio, variable=r, value=2, text="HARD", font="TimesNewRoman, 15")
hard_radio.pack(padx=25, pady=10, side=LEFT)

# radio impossible
impossible_radio = Radiobutton(background_radio, variable=r, value=3, text="IMPOSSIBLE", font="TimesNewRoman, 15")
impossible_radio.pack(padx=25, pady=10, side=RIGHT)

button_frame = Frame(root, bg="lightseagreen")
button_frame.pack(pady=20)

solve_button = Button(button_frame, text="CREATE AND SOLVE", font="TimesNewRoman, 15", command=solve_maze)
solve_button.pack(padx=50, side=LEFT)

free_turtle_button = Button(button_frame, text="RESET TURTLE", font="TimesNewRoman, 15", command=free_turtle)
free_turtle_button.pack(side=RIGHT)

if __name__ == "__main__":
    root.mainloop()
