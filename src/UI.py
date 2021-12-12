from tkinter import *
from src import ErlangModel


class MainProgram:
    def __init__(self):
        window = Tk()
        self.result_text_field = Entry()
        self.text_field_2 = Entry(bd=3)
        self.text_field_1 = Entry(bd=3)

        window.title('Erlang calculator')
        window.geometry("400x300+10+10")

        main_window_label = Label(window, text='Main window')
        main_window_label.place(x=100, y=50)
        calculator_button = Button(window, text='Calculator', command=lambda: self.calculatorWindow(window))
        calculator_button.place(x=180, y=150)

        window.mainloop()

    def clearWindow(self, window):
        for widgets in window.winfo_children():
            widgets.destroy()

    def calculateProbabilityOfBlocking(self):
        self.result_text_field.delete(0, 'end')
        average_traffic = getdouble(self.text_field_1.get())
        number_of_lines = getdouble(self.text_field_2.get())
        probability_of_blocking = round(ErlangModel.erlang_model_B(average_traffic, number_of_lines), 3)
        self.result_text_field.insert(0, str(probability_of_blocking))

    def calculatorWindow(self, window):
        self.clearWindow(window)
        average_traffic_label = Label(window, text='Average traffic')
        number_of_lines_label = Label(window, text='Number of lines')
        prob_of_blocking_label = Label(window, text='Probability of blocking')

        average_traffic_label.place(x=100, y=50)
        self.text_field_1.place(x=200, y=50)
        number_of_lines_label.place(x=100, y=100)
        self.text_field_2.place(x=200, y=100)

        calculate_button = Button(window, text='Calculate', command=lambda: self.calculateProbabilityOfBlocking)
        calculate_button.place(x=180, y=150)

        prob_of_blocking_label.place(x=70, y=200)
        self.result_text_field.place(x=200, y=200)
