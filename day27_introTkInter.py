from tkinter import *

def button_clicked():
    starting_number = input.get()
    converted = float(starting_number) * 1.609
    my_label4.config(text=f"{converted}")

window = Tk()
window.title('Mile to km Converter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text='Miles')
my_label.grid(column=2, row= 0)

# Button
button = Button(text='Convert', command=button_clicked)
button.grid(column=1, row=2)

## second-- Label
my_label2 = Label(text='is equal to')
my_label2.grid(column=0, row= 1)

## 3rd label
my_label3 = Label(text='Km', )
my_label3.grid(column=2, row= 1)

## Converted amount
my_label4 = Label(text= 0)
my_label4.grid(column=1, row= 1)

# Entry
input = Entry(width=7)
input.grid(column=1, row=0)


window.mainloop()