#calculator
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

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
def enter_number(number):
    '''display number or decimal from button'''
    #Insert number or decimal to end of display
    display.insert(END, number)
    #If decimal was entered, disable button
    if '.' in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    '''store the first number of express and operation'''
    global first_number
    global operation

    #Store first number and operation
    operation = operator
    first_number = display.get()
    display.delete(0, END)
    #Disable all operations buttons except =
    add_button.config(state=DISABLED)
    minus_button.config(state=DISABLED)
    times_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    #renable decimal button
    decimal_button.config(state=NORMAL)

def get_result():
    '''display results of operation'''
    second_number = display.get()
    if operation == 'add':
        value = float(first_number) + float(second_number)
    elif operation == 'minus':
        value = float(first_number) - float(second_number)
    elif operation == 'divide':
        if second_number == '0':
            value = 'Error'
        else:
            value = float(first_number) / float(second_number)
    elif operation == 'times':
        value = float(first_number) * float(second_number)
    elif operation == 'exponent':
        value = float(first_number) ** float(second_number)
    display.delete(0, END)
    display.insert(END, value)
    #Reenable all buttons
    enable_all_buttons()

def enable_all_buttons():
    '''reenables any buttons that had been disabled'''
    decimal_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    times_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    minus_button.config(state=NORMAL)
    add_button.config(state=NORMAL)

def clear():
    '''clear the display and reenable all buttons'''
    display.delete(0, END)
    enable_all_buttons()

def inverse():
    '''display the inverse of a number'''
    #Do not allow the inverse of 0
    number = display.get()
    if number == '0':
        value = 'Error'
    else:
        value = 1 / float(number)
    display.delete(0, END)
    display.insert(END, value)

def square():
    '''display the square of a number'''
    number = display.get()
    value = float(number) * float(number)
    display.delete(0, END)
    display.insert(END, value)



#GUI layout
#Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

#Layout of display frame
display = tkinter.Entry(display_frame, width=50, borderwidth=5, font=display_font,
                        bg=white_green, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout of button frame
#Function buttons
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=dark_green,
                              command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=dark_green,
                             command=root.destroy)
inverse_button = tkinter.Button(button_frame, text="1/x", font=button_font, bg=light_green,
                                command=inverse)
square_button = tkinter.Button(button_frame, text="x^2", font=button_font, bg=light_green,
                               command=square)
exponent_button = tkinter.Button(button_frame, text="x^n", font=button_font, bg=light_green,
                                 command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame, text="/", font=button_font, bg=light_green,
                                 command=lambda:operate('divide'))
times_button = tkinter.Button(button_frame, text="*", font=button_font, bg=light_green,
                                 command=lambda:operate('times'))
add_button = tkinter.Button(button_frame, text="+", font=button_font, bg=light_green,
                                 command=lambda:operate('add'))
minus_button = tkinter.Button(button_frame, text="-", font=button_font, bg=light_green,
                                 command=lambda:operate('minus'))
equal_button = tkinter.Button(button_frame, text="=", font=button_font, bg=dark_green,
                              command=get_result)
decimal_button = tkinter.Button(button_frame, text=".", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('.'))
negate_button = tkinter.Button(button_frame, text="+/-", font=button_font, bg='black', fg='white')
#Number buttons
zero_button = tkinter.Button(button_frame, text="0", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('0'))
one_button = tkinter.Button(button_frame, text=" 1", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('1'))
two_button = tkinter.Button(button_frame, text="2", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('2'))
three_button = tkinter.Button(button_frame, text="3", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('3'))
four_button = tkinter.Button(button_frame, text="4", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('4'))
five_button = tkinter.Button(button_frame, text="5", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('5'))
six_button = tkinter.Button(button_frame, text="6", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('6'))
seven_button = tkinter.Button(button_frame, text="7", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('7'))
eight_button = tkinter.Button(button_frame, text="8", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('8'))
nine_button = tkinter.Button(button_frame, text="9", font=button_font, bg='black', fg='white',
                             command=lambda:enter_number('9'))

#First row
clear_button.grid(row=0, column=0, columnspan=2, sticky='WE')
quit_button.grid(row=0, column=2, columnspan=2, sticky='WE')
#Second row
inverse_button.grid(row=1, column=0, pady=1, sticky='WE')
square_button.grid(row=1, column=1, pady=1, sticky='WE')
exponent_button.grid(row=1, column=2, pady=1, sticky='WE')
divide_button.grid(row=1, column=3, pady=1, sticky='WE')
#third row (the ipadx should take of filling the screen for all button rows)
seven_button.grid(row=2, column=0, pady=1, sticky='WE', ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky='WE', ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky='WE', ipadx=20)
times_button.grid(row=2, column=3, pady=1, sticky='WE', ipadx=20)
#Fourth row
four_button.grid(row=3, column=0, pady=1, sticky='WE')
five_button.grid(row=3, column=1, pady=1, sticky='WE')
six_button.grid(row=3, column=2, pady=1, sticky='WE')
minus_button.grid(row=3, column=3, pady=1, sticky='WE')
#Fifth row
one_button.grid(row=4, column=0, pady=1, sticky='WE')
two_button.grid(row=4, column=1, pady=1, sticky='WE')
three_button.grid(row=4, column=2, pady=1, sticky='WE')
add_button.grid(row=4, column=3, pady=1, sticky='WE')
#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky='WE')
zero_button.grid(row=5, column=1, pady=1, sticky='WE')
decimal_button.grid(row=5, column=2, pady=1, sticky='WE')
equal_button.grid(row=5, column=3, pady=1, sticky='WE')


#Run app
root.mainloop()
