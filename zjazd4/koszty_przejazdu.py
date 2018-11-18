import tkinter
root = tkinter.Tk()

def sumuj():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    wynik.configure(text=a*b*c/100)


a_label = tkinter.Label(master=root, text="Dystans")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text="Spalanie")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

c_label = tkinter.Label(master=root, text="Cena paliwa")
c_label.grid(row=2, column=0)
c_entry = tkinter.Entry(master=root)
c_entry.grid(row=2, column=1)


wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.grid(row=5, column=0)
wynik = tkinter.Label(master=root, text=" - ")
wynik.grid(row=5, column=1)



policz_button = tkinter.Button(master=root, text="Policz", command=sumuj)
policz_button.grid(row=5, column=6)
root.title("Koszty przejazdu")

root.mainloop()
