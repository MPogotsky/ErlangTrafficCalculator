from tkinter import *
from Calculator import Calculator
from plot import PlotProbability

if __name__ == '__main__':
    window = Tk()
    window.title('Erlang calculator')
    window.geometry("400x350+10+10")

    main_window_label = Label(window, text='Main menu', font="Helvetica 16 bold")
    main_window_label.pack(pady=50)

    calculator_button = Button(window, text='Calculator', command=lambda: Calculator(window))
    calculator_button.pack(pady=5)

    information_button = Button(window, text='Information', command=lambda: print("Information"))
    information_button.pack(pady=5)

    window.mainloop()
