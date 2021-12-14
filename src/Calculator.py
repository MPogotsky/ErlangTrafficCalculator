from tkinter import *
from src.ErlangModel import ErlangModelB


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
        self.__special_character = "-"

        self.calculatorWindow()

    def calculatorWindow(self):
        average_traffic_label = Label(self.window, text='Average traffic in Erlangs')
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
        erlang_model_b = ErlangModelB()

        self.__result_text_field.delete(0, 'end')
        average_traffic_string_field = str(self.__average_traffic_text_field.get())
        number_of_lines_string_field = str(self.__number_of_lines_text_field.get())

        if self.__check_string_for_a_delimeter(average_traffic_string_field) is True:
            min_value, max_value = average_traffic_string_field.split("-")
            average_traffic = [getdouble(min_value), getdouble(max_value)]
        else:
            average_traffic = getdouble(self.__average_traffic_text_field.get())

        if self.__check_string_for_a_delimeter(number_of_lines_string_field) is True:
            min_value, max_value = number_of_lines_string_field.split("-")
            number_of_lines = [getdouble(min_value), getdouble(max_value)]
        else:
            number_of_lines = getdouble(self.__number_of_lines_text_field.get())

        result = str(erlang_model_b.calculateProbabilityOfBlocking(average_traffic, number_of_lines))
        self.__result_text_field.insert(0, result)

    def __check_string_for_a_delimeter(self, string_field):
        if any(character in self.__special_character for character in string_field):
            return True
        else:
            return False
