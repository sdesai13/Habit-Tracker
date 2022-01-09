from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox
from tkmacosx import Button
from tkinter import ttk
import PIL
from PIL import ImageTk,Image


root = Tk()
root.title("Habit Tracker")

root.iconphoto(True, PhotoImage(file="running.png"))

root.resizable(False, False)
root.config(pady=50, padx=50, background="lightblue")
URL = "[enter your graph url]"
TODAY = dt.now()


style = ttk.Style(root)
style.theme_use('clam')

pagetitle = Label( text="Habit Tracker", border=0, bg="lightblue",fg="red", font=(None,30,"bold")).place(x=135,
                                         y=-43)


def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    token = "[enter your token]"
    headers = {"X-USER-TOKEN": token}
    endpoint = "https://pixe.la/v1/users/sampleprofile12/graphs/graph1/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def del_pixel():
    endpoint = f"https://pixe.la/v1/users/sampleprofile12/graphs/graph1/{format_date()}"
    token = "[enter your token]"
    headers = {"X-USER-TOKEN": token}
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Pixel deleted.")


def change_pixel():
    endpoint = f"https://pixe.la/v1/users/sampleprofile12/graphs/graph1/{format_date()}"
    token = "[enter your token]"
    headers = {"X-USER-TOKEN": token}

    pixel_update = {
        "quantity": user_in.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")
print(style.theme_names())

cal = Calendar(root, background="white", disabledbackground="red", bordercolor="red",
               headersbackground="red", normalbackground="white", foreground='red',
               normalforeground='red', headersforeground='white')
cal.grid(row=0, column=0, columnspan=10,)

units = Label(text="KM Ran:", border=0, bg = "red", fg="white", )
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_in = Entry(width=10, border=0.5, highlightbackground="red")
user_in.grid(row=1, column=2, sticky="w",padx=4.5,)

TOKEN = "YOUR TOKEN"
GRAPH_ID = "YOUR GRAPH_ID"

headers = {
    "X-USER-TOKEN": TOKEN
}

add = Button(text="Add", command=add_pixel, bg="red", fg="white", borderless=1 )
add.grid(row=2, column=0, pady=5, padx=5)

update = Button(text="Update", command=change_pixel, bg="red", fg="white", borderless=1)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel,bg="red", fg="white", borderless=1)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nGraph", command=open_browser, bg ="red", fg="white", borderless=1)
link.grid(row=2, column=3)

root.mainloop()