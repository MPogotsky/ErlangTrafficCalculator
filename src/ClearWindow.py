def clear_window(window):
    for widgets in window.winfo_children():
        widgets.destroy()
