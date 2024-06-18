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

#GUI layout
#Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack()
button_frame.pack()

#Layout of display frame
display = tkinter.Entry(display_frame, width=50, borderwidth=5, font=display_font,
                        bg=white_green, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout of button frame
#Function buttons
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=dark_green)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=dark_green)
inverse_button = tkinter.Button(button_frame, text="1/x", font=button_font, bg=light_green)
square_button = tkinter.Button(button_frame, text="x^2", font=button_font, bg=light_green)
exponent_button = tkinter.Button(button_frame, text="x^n", font=button_font, bg=light_green)
divide_button = tkinter.Button(button_frame, text=" / ", font=button_font, bg=light_green)
times_button = tkinter.Button(button_frame, text=" * ", font=button_font, bg=light_green)
add_button = tkinter.Button(button_frame, text=" + ", font=button_font, bg=light_green)
minus_button = tkinter.Button(button_frame, text=" - ", font=button_font, bg=light_green)
equal_button = tkinter.Button(button_frame, text=" = ", font=button_font, bg=dark_green)
decimal_button = tkinter.Button(button_frame, text=" . ", font=button_font, bg='black', fg='white')
negate_button = tkinter.Button(button_frame, text="+/-", font=button_font, bg='black', fg='white')
#Number buttons
zero_button = tkinter.Button(button_frame, text=" 0 ", font=button_font, bg='black', fg='white')
one_button = tkinter.Button(button_frame, text="  1 ", font=button_font, bg='black', fg='white')
two_button = tkinter.Button(button_frame, text=" 2 ", font=button_font, bg='black', fg='white')
three_button = tkinter.Button(button_frame, text=" 3 ", font=button_font, bg='black', fg='white')
four_button = tkinter.Button(button_frame, text=" 4 ", font=button_font, bg='black', fg='white')
five_button = tkinter.Button(button_frame, text=" 5 ", font=button_font, bg='black', fg='white')
six_button = tkinter.Button(button_frame, text=" 6 ", font=button_font, bg='black', fg='white')
seven_button = tkinter.Button(button_frame, text=" 7 ", font=button_font, bg='black', fg='white')
eight_button = tkinter.Button(button_frame, text=" 8 ", font=button_font, bg='black', fg='white')
nine_button = tkinter.Button(button_frame, text=" 9 ", font=button_font, bg='black', fg='white')

#First row
clear_button.grid(row=0, column=0)
quit_button.grid(row=0, column=1)
#Second row
inverse_button.grid(row=1, column=0)
square_button.grid(row=1, column=1)
exponent_button.grid(row=1, column=2)
divide_button.grid(row=1, column=3)
#third row
seven_button.grid(row=2, column=0)
eight_button.grid(row=2, column=1)
nine_button.grid(row=2, column=2)
times_button.grid(row=2, column=3)
#Fourth row
four_button.grid(row=3, column=0)
five_button.grid(row=3, column=1)
six_button.grid(row=3, column=2)
minus_button.grid(row=3, column=3)
#Fifth row
one_button.grid(row=4, column=0)
two_button.grid(row=4, column=1)
three_button.grid(row=4, column=2)
add_button.grid(row=4, column=3)
#Sixth row
negate_button.grid(row=5, column=0)
zero_button.grid(row=5, column=1)
decimal_button.grid(row=5, column=2)
equal_button.grid(row=5, column=3)


#Run app
root.mainloop()
