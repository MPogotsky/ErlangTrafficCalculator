from tkinter import *
from src import ErlangModel


def clearWindow(window):
    for widgets in window.winfo_children():
        widgets.destroy()


class Calculator:
    def __init__(self, window):
        clearWindow(window)
        self.window = window
        self.__average_traffic_text_field = Entry(bd=3)
        self.__number_of_lines_text_field = Entry(bd=3)
        self.__result_text_field = Entry()

        self.calculatorWindow()

    def calculatorWindow(self):
        average_traffic_label = Label(self.window, text='Average traffic')
        number_of_lines_label = Label(self.window, text='Number of lines')
        prob_of_blocking_label = Label(self.window, text='Probability of blocking')

        average_traffic_label.place(x=100, y=50)
        self.__average_traffic_text_field.place(x=200, y=50)
        number_of_lines_label.place(x=100, y=100)
        self.__number_of_lines_text_field.place(x=200, y=100)

        calculate_button = Button(self.window, text='Calculate', command=self.calculateTheResult)
        calculate_button.place(x=180, y=150)

        prob_of_blocking_label.place(x=70, y=200)
        self.__result_text_field.place(x=200, y=200)

    def calculateTheResult(self):
        self.__result_text_field.delete(0, 'end')
        average_traffic = getdouble(self.__average_traffic_text_field.get())
        number_of_lines = getdouble(self.__number_of_lines_text_field.get())
        self.__result_text_field.insert(0,
                                        str(ErlangModel.calculateProbabilityOfBlocking(average_traffic,
                                                                                       number_of_lines)))
