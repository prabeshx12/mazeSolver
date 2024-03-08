import turtle
import tkinter as tk

def start_turtle():
    # Create a new Tkinter window
    new_window = tk.Toplevel(root)
    new_window.title("Turtle with Tkinter")

    # Create a Turtle screen
    screen = turtle.Screen()

    # Create a Turtle
    t = turtle.Turtle()

    # Draw something on the screen
    t.forward(100)
    t.left(90)
    t.forward(100)

    # Bind the screen's destroy event to a function that closes both windows
    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", lambda: close_windows(new_window))

def close_windows(window):
    window.destroy()
    turtle.bye()

# Create Tkinter window
root = tk.Tk()
root.title("Main Window")

# Button to start Turtle graphics
start_button = tk.Button(root, text="Start Turtle", command=start_turtle)
start_button.pack()

# Run Tkinter event loop
root.mainloop()
