from tkinter import *
from tkinter import messagebox
from src.ErlangModel import ErlangModelB
from src.ClearWindow import clear_window


class Calculator:
    def __init__(self, parent, window):
        clear_window(window)
        self.window = window
        self.__average_traffic_text_field = Entry(bd=3)
        self.__number_of_lines_text_field = Entry(bd=3)
        self.__result_text_field = Entry()
        self.__special_character = "-"

        self.__create__window(parent)

    def __create__window(self, parent):
        average_traffic_label = Label(self.window, text='Average traffic in Erlangs')
        average_traffic_label.pack(pady=20)
        self.__average_traffic_text_field.pack()

        number_of_lines_label = Label(self.window, text='Number of lines')
        number_of_lines_label.pack(pady=20)
        self.__number_of_lines_text_field.pack()

        calculate_button = Button(self.window, text='Calculate', command=self.__calculate__the__result)
        calculate_button.pack(pady=20)

        back_button = Button(self.window, text='Back', command=lambda: self.__back_to_main(parent))

        prob_of_blocking_label = Label(self.window, text='Probability of blocking')
        prob_of_blocking_label.pack()
        self.__result_text_field.pack()
        back_button.pack(pady=20)

    def __calculate__the__result(self):
        erlang_model_b = ErlangModelB()

        self.__result_text_field.delete(0, 'end')
        average_traffic_string_field = str(self.__average_traffic_text_field.get())
        number_of_lines_string_field = str(self.__number_of_lines_text_field.get())

        average_traffic = None
        number_of_lines = None

        if self.__filed_data_is_ok(average_traffic_string_field):
            average_traffic = self.__get_average_traffic_from(average_traffic_string_field)
        else:
            messagebox.showwarning('Warning', 'Bad value of Average traffic')

        if self.__filed_data_is_ok(number_of_lines_string_field):
            number_of_lines = self.__get_average_traffic_from(number_of_lines_string_field)
        else:
            messagebox.showwarning('Warning', 'Bad value of Number of lines')

        if average_traffic and number_of_lines:
            result = str(erlang_model_b.calculate_probability_of_blocking(average_traffic, number_of_lines))
            result = result.translate({ord(i): None for i in '[]'})
            self.__result_text_field.insert(0, result)

    def __get_average_traffic_from(self, average_traffic_string_field):
        if self.__check_string_for_a_delimeter(average_traffic_string_field) is True:
            min_value, max_value = average_traffic_string_field.split(self.__special_character)
            average_traffic = [getint(min_value), getint(max_value)]
        else:
            average_traffic = getint(average_traffic_string_field)
        return average_traffic

    def __get_number_of_lines_from(self, number_of_lines_string_field):
        if self.__check_string_for_a_delimeter(number_of_lines_string_field) is True:
            min_value, max_value = number_of_lines_string_field.split(self.__special_character)
            number_of_lines = [getint(min_value), getint(max_value)]
        else:
            number_of_lines = getint(number_of_lines_string_field)
        return number_of_lines

    def __filed_data_is_ok(self, string_field):
        if self.__check_string_for_a_delimeter(string_field) is True:
            min_value, max_value = string_field.split(self.__special_character)
            if min_value.isnumeric() and max_value.isnumeric():
                min_value, max_value = getint(min_value), getint(max_value)
                if min_value > 0 and max_value > 0:
                    return True
        else:
            if string_field.isnumeric():
                number = getint(string_field)
                if number > 0:
                    return True
        return False

    def __check_string_for_a_delimeter(self, string_field):
        if any(character in self.__special_character for character in string_field):
            return True
        else:
            return False

    def __back_to_main(self, parent):
        clear_window(self.window)
        parent(self.window)
