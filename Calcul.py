import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text = "+", width = 4, height = 3)
button_sub = tk.Button(window, text = '-', width = 4, height = 3)
button_mul = tk.Button(window, text = '*', width = 4, height = 3)
button_div = tk.Button(window, text = '/', width = 4, height = 3)
button_sub.place(x = 110, y = 250)
button_add.place(x = 60, y = 250)
button_mul.place(x = 160, y = 250)
button_div.place(x = 210, y = 250)
window.mainloop()
