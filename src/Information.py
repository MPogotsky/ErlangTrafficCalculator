from tkinter import *
from tkhtmlview import HTMLLabel
import codecs


def clearWindow(window):
    for widgets in window.winfo_children():
        widgets.destroy()


class Information:
    def __init__(self, parent, window):
        clearWindow(window)
        self.window = window
        self.window.geometry("610x750+10+10")
        self.createWindow(parent)

    def createWindow(self, parent):

        html_file = codecs.open("dependency/help.htm", "r").read()

        html_view = HTMLLabel(self.window, html=html_file)

        back_button = Button(self.window, text='Back', height=1, width=6, command=lambda: self.__back_to_main(parent))
        back_button.pack(side=BOTTOM, pady=3)

        html_view.fit_height()
        html_view.pack(pady=3, expand=True)

    def __back_to_main(self, parent):
        clearWindow(self.window)
        self.window.geometry("500x450+10+10")
        parent(self.window)
