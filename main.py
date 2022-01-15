from tkinter import *
from src.Calculator import Calculator


def controller(window):
    main_window_label = Label(window, text='Main menu', font="Helvetica 16 bold")
    main_window_label.pack(pady=50)

    calculator_button = Button(window, text='Calculator', command=lambda: Calculator(controller, window))
    calculator_button.pack(pady=5)

    information_button = Button(window, text='Information', command=lambda: print("Information"))
    information_button.pack(pady=5)


if __name__ == '__main__':
    main_window = Tk()
    main_window.title('Erlang calculator')
    main_window.geometry("400x350+10+10")
    controller(main_window)
    main_window.mainloop()

