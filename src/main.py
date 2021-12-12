from tkinter import *
from src import UI
from Calculator import Calculator

if __name__ == '__main__':
    window = Tk()
    window.title('Erlang calculator')
    window.geometry("400x300+10+10")

    main_window_label = Label(window, text='Main window')
    main_window_label.place(x=100, y=50)
    calculator_button = Button(window, text='Calculator', command=lambda: Calculator(window))
    calculator_button.place(x=180, y=150)

    window.mainloop()
