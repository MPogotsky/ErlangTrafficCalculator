from tkinter import *
from matplotlib.figure import Figure, GridSpec, Axes
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


class Graph:
    def __init__(self, dependency_array, dependency_array_name,  probability_of_blocking):
        self.x_values = dependency_array
        self.x_axes_label = dependency_array_name
        self.y_values = probability_of_blocking
        self.__graphWindow()

    def __graphWindow(self):
        window = Tk()
        window.title('Probability of blocking')
        window.geometry("708x766")
        self.__plotGraph(window)
        window.mainloop()

    def __plotGraph(self, window):
        figure = Figure(figsize=(7, 7), dpi=100)
        plot_graph = figure.add_subplot(111)

        plot_graph.plot(self.x_values, self.y_values)
        min_value = min(self.x_values)
        max_value = max(self.x_values)
        title = "Probability of blocking for " + str(self.x_axes_label) + " " + str(min_value) + "-" + str(max_value)
        plot_graph.set_title(title)
        plot_graph.grid()
        plot_graph.set_xlabel(self.x_axes_label)
        plot_graph.set_ylabel("Probability of blocking")

        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.draw()

        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()

        canvas.get_tk_widget().pack()
