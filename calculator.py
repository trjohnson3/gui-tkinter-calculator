#calculator
import tkinter
from tkinter import RIGHT

#Define window
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('./images/calculator.ico')
root.geometry('300x400')
root.resizable(0, 0)

#Define fonts and colors
dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'
button_font = ('Arial', 18)
display_font = ('Arial', 30)

#Define funcitons

#Define layout
#Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack()
button_frame.pack()

#Layout of display frame
display = tkinter.Entry(display_frame, width=50, borderwidth=5, font=display_font,
                        bg=white_green, justify=RIGHT)
display.pack(padx=5, pady=5)

#Run app
root.mainloop()
