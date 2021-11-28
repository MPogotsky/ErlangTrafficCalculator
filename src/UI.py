from tkinter import *
import ErlangModel


class MainProgram:
    def __init__(self):
        window = Tk()
        window.title('Erlang calculator')
        window.geometry("400x300+10+10")

        self.label_1 = Label(window, text='Average traffic')
        self.label_2 = Label(window, text='Number of lines')
        self.label_3 = Label(window, text='Probability of blocking')

        self.text_field_1 = Entry(bd=3)
        self.text_field_2 = Entry(bd=3)
        self.text_field_3 = Entry()

        self.button_1 = Button(window, text='Calculate')

        self.label_1.place(x=100, y=50)
        self.text_field_1.place(x=200, y=50)
        self.label_2.place(x=100, y=100)
        self.text_field_2.place(x=200, y=100)

        b1 = Button(window, text='Calculate', command=self.calculate)

        b1.place(x=180, y=150)
        self.label_3.place(x=70, y=200)
        self.text_field_3.place(x=200, y=200)

        window.mainloop()

    def calculate(self):
        self.text_field_3.delete(0, 'end')
        average_traffic = getdouble(self.text_field_1.get())
        number_of_lines = getdouble(self.text_field_2.get())
        probability_of_blocking = round(ErlangModel.erlang_model_B(average_traffic, number_of_lines), 3)
        self.text_field_3.insert(0, str(probability_of_blocking))
