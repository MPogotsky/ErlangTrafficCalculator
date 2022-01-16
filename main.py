from tkinter import *
from src.Calculator import Calculator
from src.Information import Information


def controller(window):
    main_window_label = Label(window, text='Erlang Traffic Calculator \n\n', font="Helvetica 16 bold")
    main_window_label.pack(pady=50)

    calculator_button = Button(window, text='Calculator', height=3, width=20,
                               command=lambda: Calculator(controller, window))
    calculator_button.pack(pady=5)

    information_button = Button(window, text='Help', height=3, width=20,
                                command=lambda: Information(controller, window))
    information_button.pack(pady=5)

    creator_text = Label(window, text='by Matsvei Pahotski, 2022', font="Helvetica 9")
    creator_text.pack(side=BOTTOM)


if __name__ == '__main__':
    main_window = Tk()
    main_window.iconbitmap("dependency/pwr.ico")
    main_window.title("Erlang calculator")
    main_window.geometry("500x450+10+10")
    controller(main_window)
    main_window.mainloop()
