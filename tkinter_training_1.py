#import
import tkinter as tkinter
window = tk.Tk()

#greeting
greeting = tkinter.Label(text='Hello, Tkinter')
greeting.pack()
window.mainloop()

#exercise1
exercise1 = tkinter.Lable(text='Python Rocks!')
exercise1.pack()
window.mainloop()

#coloring the window, words
label = tkinter.Label(
    text = "Hello, Tkinter"
    foreground = "white"
    background = "black"
)

#coloring the windows, hexadecimals RGB values
label = tkinter.Label(text = "Hello, Tkinter", background = "#34A2FE")
label = tkinter.Label(text = "Hello, Tkinter" fg = "white", bg = "black")
