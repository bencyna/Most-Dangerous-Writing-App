from tkinter import *
from tkinter import ttk

window = Tk()
window.config(padx=50, pady=50, width=900, height=700, background='white')
window.title("Writers block block")

started = False
red = False


def user_typing():
    global clear_warning, clear_game, started, red
    if not started:
        started = True
    if red:
        text.configure(foreground='black')

    window.after_cancel(clear_warning)
    window.after_cancel(clear_game)
    clear_warning = window.after(4000, warning_limit)
    clear_game = window.after(5000, game_finished)


# ToDo 1. Setup the screen
# has an input
frame = Frame(borderwidth=5, relief=SUNKEN)
frame.pack()

text = Text(width=50, font=('Times New Roman', 15, 'italic'), borderwidth=0)
text.insert(INSERT, "Start typing...")

style = ttk.Style()
style.configure('TEntry', foreground='black')
# text.focus()
text.pack(side=TOP, ipadx=30, ipady=10)

text.bind("<FocusIn>", lambda args: text.delete("1.0", 'end'))
text.bind('<KeyPress>', lambda args: user_typing())

canvas = Canvas(width=900, height=600, highlightthickness=0, background="white")
canvas.pack()


# ToDo 2. Setup a 5 second timer
def game_finished():
    if started:
        text.delete("1.0", 'end')


# If timer = 0 set the text to empty
# If timer = 1 srt text to red
def warning_limit():
    global started, red
    if started:
        red = True
        text.configure(foreground='red')


clear_warning = window.after(4000, warning_limit)
clear_game = window.after(5000, game_finished)

window.mainloop()
