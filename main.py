from tkinter import *

window = Tk()
window.config(padx=50, pady=50, width=900, height=700, background='white')
window.title("Writers block block")
canvas = Canvas(width=900, height=600, highlightthickness=0, background="white")
canvas.pack()


# ToDo 1. Setup the screen
#has an input
text = Entry(width=21, placeholder="Start Typing..")
text.focus()
text.place(x=400, y=0)

text.bind("<FocusIn>", lambda args: text.delete('0', 'end'))

# ToDo 2. Setup a 5 second timer
# If timer = 0 set the text to empty
# If timer = 1 srt text to red

window.mainloop()
