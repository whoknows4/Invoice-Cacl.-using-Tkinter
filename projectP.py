from tkinter import *
import datetime as dt

# grid() helps to arrange widgets in table like structure

window = Tk()
window.geometry("800x800")
window.title("TAX INVOICE")

logo = PhotoImage(file="icon.png")

# tax invoice
invoice = Label(window, text="(TAX INVOICE)", font=("Arial", 15))     # tax invoice 
invoice.place(x=400, y=20, anchor="center")

# logo
lago = Label(window, image=logo)
lago.place(x=660, y=50)                   

# rk arts 
heading = Label(window, text="RK arts", font=("Arial", 30, "bold"))
heading.place(x=500, y=50)

# address
addr = Label(window, text="356 A1A 4B Hosayallapur Road", font=("Arial"))
addr.place(x=420, y=100)

# address2
addr1 = Label(window, text="Ramnagar, Dharwad", font=("Arial"))
addr1.place(x=500, y=130)

# email, mobile vagera vagera
emailmob = Label(window, text="M:9964917641, rkartsdwd@gmail.com", font=("Arial"))
emailmob.place(x=380, y=160)

# gst number
gstin = Label(window, text="GSTIN:29EQMPP0275C1ZM", font=("Arial", 15, "bold"))
gstin.place(x=10, y=50)

# that blue line
bline = Entry(window, bg="blue", width=32)
bline.place(x=10, y = 74)

# venue label
place = Label(window, text="To, ", font=("Arial"))
place.place(x=10, y=200)

# venue 
venue = Entry(window, width=52)
venue.place(x=10, y=220)

# label to display date
date = dt.datetime.now()
ddate = Label(window, text=f"Date: {date:%b-%d-20%y}")
ddate.place(x=670, y=220)

# invoice number 
inum = Label(window, text="Invoice No. ")
inum.place(x=540, y=220)
inv_label = Entry(window, width=3)
inv_label.place(x=620, y=220)

window.mainloop()