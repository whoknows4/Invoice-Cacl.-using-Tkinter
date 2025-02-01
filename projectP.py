from tkinter import *
from tkinter import ttk
from num2words import num2words
import datetime as dt

# grid() helps to arrange widgets in table like structure

window = Tk()
window.geometry("800x1000")
window.title("TAX INVOICE")

logo = PhotoImage(file="icon.png")

invoice_ = []

def addItem():
    s_no = sno_entry.get()
    descrip = desc_entry.get()
    quantity = int(quan_entry.get())
    rte = float(rate_entry.get())
    pr = per_entry.get()
    amount = quantity * rte

    tree.insert("", END, values=(s_no, descrip, quantity, rte, pr, f"{amount:.2f}"))

    invoice_.append(amount)
    
    update_total()

    sno_entry.delete(0, END)   
    desc_entry.delete(0, END)
    quan_entry.delete(0, END)
    rate_entry.delete(0, END)
    per_entry.delete(0, END)

def update_total():
    amt_total = sum(invoice_)
    cgst = amt_total * 0.09
    sgst = amt_total * 0.09
    total = amt_total + cgst + sgst

    amt.config(text=f"Sub-Total: {amt_total:.2f}")
    cgst_tag.config(text=f"CGST 9%: {cgst:.2f}")
    sgst_tag.config(text=f"SGST 9%: {sgst:.2f}")
    total_tag.config(text=f"TOTAL:  {total:.2f}")
    
    only_int = int(total)
    words = num2words(only_int).upper()
    n2w_label.config(text=f" {words:}")


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

# user input fields
# sl.no. field
sno = Label(window, text="Sl.No.")
sno.place(x=10, y=270)

sno_entry = Entry(window, width=3)
sno_entry.place(x=10, y=290)

# description field
desc = Label(window, text="Description")
desc.place(x=60, y=270)

desc_entry = Entry(window, width=25)
desc_entry.place(x=60, y=290)

# quantity
quan = Label(window, text="Quantity")
quan.place(x=280, y=270)

quan_entry = Entry(window, width=3)
quan_entry.place(x=280, y=290)

# rate
rate = Label(window, text="Rate")
rate.place(x=350, y=270)

rate_entry = Entry(window, width=12)
rate_entry.place(x=350, y=290)

# per
per = Label(window, text="Per")
per.place(x=470, y=270)

per_entry = Entry(window, width=15)
per_entry.place(x=470, y=290)

# add button
add_button = Button(window, text="Ad Item", command=addItem)
add_button.place(x=660, y=290)

# treeview function 
columns = ("Sl.No.", "Description", "Quantity", "Rate", "Per", "Amount")
tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=20)

tree.place(x=10, y=350, width=780, height=350)

# sub total
amt = Label(window, text="Sub-Total: ", font=("Arial", 13, "bold"))
amt.place(x=580, y=700)

# cgst
cgst_tag = Label(window, text="CGST 9%: ", font=("Arial", 13, "bold"))
cgst_tag.place(x=580, y=720)

# sgst
sgst_tag = Label(window, text="SGST 9%: ", font=("Arial", 13, "bold"))
sgst_tag.place(x=580, y=740)

# total
total_tag = Label(window, text="TOTAL: ", font=("Arial", 13, "bold"))
total_tag.place(x=580, y=760)

# number to word
n2w = Label(window, text="In Words: ", font=("Arial",15 ,"bold"))
n2w.place(x=10, y=720)

n2w_label = Label(window, text="", font=("Arial", 12, "bold"))
n2w_label.place(x=10, y=750)

# last label entries
please = Label(window, text="Please ackowledge the receipt of the invoices and kindly release the payment at the earliest and oblige.", font=("Arial", 10))
please.place(x=10, y=790)

terms = Label(window, text="Terms & Conditions :", font=("Arial", 10, "bold"))
terms.place(x=10, y=810)

alll = Label(window, text="• All payments are to be made  to RK ARTS by  Cheque/DD(Crossed Account Payee Only)", font=("Arial", 10))
alll.place(x=10, y=830)

iner = Label(window, text="• Interest will be charged @ 2% per month after the due date", font=("Arial", 10))
iner.place(x=10, y=850)

# firm bank detals
firm = Label(window, text="Firm Bank Details", font=("Arial", 12, "bold"))
firm.place(x=10, y=880)

ac = Label(window, text="A/C Name :", font=("Arial", 12))
ac.place(x=10, y=900)
ac_ = Label(window, text="RK ARTS", font=("Arial", 12, "bold"))
ac_.place(x=100, y=900)

acno = Label(window, text="A/C No      :", font=("Arial", 12))
acno.place(x=10, y=920)
acno_ = Label(window, text="5742085338", font=("Arial", 12, "bold"))
acno_.place(x=100, y=920)

benk = Label(window, text="Bank          :", font=("Arial", 12))
benk.place(x=10, y=940)
benk_ = Label(window, text="CENTRAL BANK DHARWAD", font=("Arial", 12, "bold"))
benk_.place(x=100, y=940)

ifs = Label(window, text="IFS CODE :", font=("Arial", 12))
ifs.place(x=10, y=960)
ifs_ = Label(window, text="CBIN0283371", font=("Arial", 12, "bold"))
ifs_.place(x=100, y=960)

subj = Label(window, text="Subject to Dharwad Jurisdiction", font=("Arial", 10))
subj.place(x=300, y=980)

fa = Label(window, text="For: RK arts", font=("Arial", 13, "bold"))
fa.place(x=640, y=840)
fa_ = Label(window, text="Proprietor", font=("Arial", 10, "bold"))
fa_.place(x=660, y=910)

window.mainloop()