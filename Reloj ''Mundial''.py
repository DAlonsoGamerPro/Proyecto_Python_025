from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("700x900")
root.title("Reloj ''Mundial''")

india_image = ImageTk.PhotoImage(Image.open("india.jpg"))
usa_image = ImageTk.PhotoImage(Image.open("usa.jpg"))
japan_image = ImageTk.PhotoImage(Image.open("japan.jpg"))
australia_image = ImageTk.PhotoImage(Image.open("australia.jpg"))

#__________________*INDIA*__________________#
india_label = Label(root,text="India")
india_label.place(relx=0.25,rely=0.02,anchor=CENTER)
india_map = Label(root)
india_map["image"] = india_image
india_map.place(relx=0.25,rely=0.21,anchor=CENTER)
india_time = Label(root)
india_time.place(relx=0.25,rely=0.4,anchor=CENTER)


#__________________*U.S.A.*__________________#
usa_label = Label(root,text="usa")
usa_label.place(relx=0.75,rely=0.02,anchor=CENTER)
usa_map = Label(root)
usa_map["image"] = usa_image
usa_map.place(relx=0.75,rely=0.21,anchor=CENTER)
usa_time = Label(root)
usa_time.place(relx=0.75,rely=0.4,anchor=CENTER)


#__________________*JAPAN*__________________#
japan_label = Label(root,text="japan")
japan_label.place(relx=0.75,rely=0.5,anchor=CENTER)
japan_map = Label(root)
japan_map["image"] = japan_image
japan_map.place(relx=0.75,rely=0.69,anchor=CENTER)
japan_time = Label(root)
japan_time.place(relx=0.75,rely=0.88,anchor=CENTER)


#__________________*AUSTRALIA*__________________#
australia_label = Label(root,text="australia")
australia_label.place(relx=0.25,rely=0.5,anchor=CENTER)
australia_map = Label(root)
australia_map["image"] = australia_image
australia_map.place(relx=0.25,rely=0.69,anchor=CENTER)
australia_time = Label(root)
australia_time.place(relx=0.25,rely=0.88,anchor=CENTER)

root.mainloop()