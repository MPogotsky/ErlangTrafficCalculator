from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf


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
        pdf_frame = pdf.ShowPdf()
        pdf_window = pdf_frame.pdf_view(self.window, pdf_location=r"description.pdf", width=100, height=50)

        back_button = Button(self.window, text='Back', command=lambda: self.__back_to_main(parent))
        back_button.pack(pady=20)

        pdf_window.pack()

    def __back_to_main(self, parent):
        clearWindow(self.window)
        self.window.geometry("500x450+10+10")
        parent(self.window)
