import tkinter as tk
window = tk.Tk()
window.geometry('200x70')
etiket = tk.Label(text='Merhaba Zalim Dünya')
etiket.pack()
button = tk.Button(text='Tamam', command=window.destroy)
button.pack()
window.mainloop()

