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
        average_traffic_label.pack(pady=20)
        self.__average_traffic_text_field.pack()

        number_of_lines_label = Label(self.window, text='Number of lines')
        number_of_lines_label.pack(pady=20)
        self.__number_of_lines_text_field.pack()

        calculate_button = Button(self.window, text='Calculate', command=self.calculateTheResult)
        calculate_button.pack(pady=20)

        prob_of_blocking_label = Label(self.window, text='Probability of blocking')
        prob_of_blocking_label.pack()
        self.__result_text_field.pack()

    def calculateTheResult(self):
        self.__result_text_field.delete(0, 'end')
        average_traffic = getdouble(self.__average_traffic_text_field.get())
        number_of_lines = getdouble(self.__number_of_lines_text_field.get())
        self.__result_text_field.insert(0,
                                        str(ErlangModel.calculateProbabilityOfBlocking(average_traffic,
                                                                                       number_of_lines)))
