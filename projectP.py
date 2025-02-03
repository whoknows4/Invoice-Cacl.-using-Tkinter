import json
from tkinter import *
from tkinter import ttk, messagebox
from num2words import num2words
import datetime as dt
from fpdf import FPDF


INVOICE_NUMBER_FILE = "invoice_number.json"

def get_next_invoice_number():
    try:
        with open(INVOICE_NUMBER_FILE, "r") as file:
            data = json.load(file)
            last_number = data.get("last_invoice_number", 0)
        
        next_number = last_number + 1
        
        with open(INVOICE_NUMBER_FILE, "w") as file:
            json.dump({"last_invoice_number": next_number}, file)
        
        return next_number
    except FileNotFoundError:
        
        with open(INVOICE_NUMBER_FILE, "w") as file:
            json.dump({"last_invoice_number": 1}, file)
        return 1
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

def export_to_pdf():
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("TimesNewRoman", "", "times.ttf", uni=True) 
        pdf.add_font("TimesNewRomanB", "", "timesbd.ttf", uni=True)

        if logo:
            pdf.image("icon.png", x=160, y=10, w=30)

        pdf.set_font("TimesNewRomanB", size=25)
        pdf.cell(150, 10, txt="RK Arts", ln=False, align="R")
        pdf.set_font("TimesNewRoman", size=10) 
        pdf.cell(0, 10, txt="", ln=True)

    
        pdf.cell(150, 10, txt="356 A1A 4B Hosayallapur Road", ln=False, align="R")
        pdf.cell(0, 5, txt="", ln=True)  
        pdf.cell(150, 10, txt="Ramnagar, Dharwad", ln=False, align="R")
        pdf.cell(0, 5, txt="", ln=True)  
        pdf.cell(150, 10, txt="M: 9964917641, rkartsdwd@gmail.com", ln=False, align="R")
        pdf.cell(0, 5, txt="", ln=True)  


        pdf.set_font("TimesNewRomanB", size=14)
        pdf.cell(0, 5, txt="GSTIN: 29EQMPP0275C1ZM", ln=True, align="L")
        pdf.set_fill_color(0, 0, 255)
        pdf.cell(65, 2, txt="", ln=True, fill=True) 
        
        pdf.cell(0, 5, txt="", ln=True)  

        pdf.set_font("TimesNewRoman", size=10)
        pdf.cell(180, 0, txt=f"Date: {date:%b-%d-20%y}", ln=True, align="R")
        pdf.cell(140, 0, txt=f"Invoice No: {invoice_number}", ln=True, align="R")
        pdf.cell(0, 0, txt=f"To: {venue.get()}", ln=True, align="L")
        
        pdf.cell(0, 5, txt="", ln=True)  
        
        pdf.set_font("TimesNewRomanB", size=10)
        pdf.cell(20, 10, txt="Sl.No.", border=1, align="C")
        pdf.cell(70, 10, txt="Description", border=1, align="C")
        pdf.cell(20, 10, txt="Quantity", border=1, align="C")
        pdf.cell(20, 10, txt="Rate", border=1, align="C")
        pdf.cell(20, 10, txt="Per", border=1, align="C")
        pdf.cell(30, 10, txt="Amount", border=1, ln=True, align="C")
        
        pdf.set_font("TimesNewRoman", size=10)
        for row in tree.get_children():
            item = tree.item(row)["values"]
            pdf.cell(20, 10, txt=str(item[0]), border=1, align="C")
            pdf.cell(70, 10, txt=str(item[1]), border=1, align="L")
            pdf.cell(20, 10, txt=str(item[2]), border=1, align="C")
            pdf.cell(20, 10, txt=str(item[3]), border=1, align="C")
            pdf.cell(20, 10, txt=str(item[4]), border=1, align="C")
            pdf.cell(30, 10, txt=str(item[5]), border=1, ln=True, align="C")

        pdf.set_font("TimesNewRomanB", size=12)
        pdf.cell(160, 10, txt="Sub-Total:", border=0, align="R")
        pdf.cell(30, 10, txt=amt.cget("text").split(": ")[1], border=0, ln=True, align="C")
        pdf.cell(160, 10, txt="CGST 9%:", border=0, align="R")
        pdf.cell(30, 10, txt=cgst_tag.cget("text").split(": ")[1], border=0, ln=True, align="C")
        pdf.cell(160, 10, txt="SGST 9%:", border=0, align="R")
        pdf.cell(30, 10, txt=sgst_tag.cget("text").split(": ")[1], border=0, ln=True, align="C")
        pdf.cell(160, 10, txt="TOTAL:", border=0, align="R")
        pdf.cell(30, 10, txt=total_tag.cget("text").split(": ")[1], border=0, ln=True, align="C")

        pdf.set_font("TimesNewRomanB", size=12)
        pdf.cell(0, 10, txt=f"In Words: {n2w_label.cget('text')}", ln=True, align="L")

        pdf.set_font("TimesNewRoman", size=9)
        pdf.cell(0, 10, txt="Please acknowledge the receipt of the invoices and kindly release the payment at the earliest and oblige.", ln=True, align="L")
        pdf.set_font("TimesNewRomanB", size=9)
        pdf.cell(0, 10, txt="Terms & Conditions:", ln=True, align="L")
        pdf.set_font("TimesNewRoman", size=9) 
        pdf.cell(0, 10, txt="• All payments are to be made to RK Arts by Cheque/DD (Crossed Account Payee Only).", ln=True, align="L")
        pdf.cell(0, 10, txt="• Interest will be charged @ 2% per month after the due date.", ln=True, align="L")

        pdf.set_font("TimesNewRomanB", size=12)  
        pdf.cell(0, 10, txt="Firm Bank Details", ln=True, align="L")
        pdf.set_font("TimesNewRoman", size=10) 
        pdf.cell(0, 10, txt="A/C Name: RK Arts", ln=True, align="L")
        pdf.cell(0, 10, txt="A/C No: 5742085338", ln=True, align="L")
        pdf.cell(0, 10, txt="Bank: Central Bank Dharwad", ln=True, align="L")
        pdf.cell(0, 10, txt="IFS Code: CBIN0283371", ln=True, align="L")

        pdf.set_font("TimesNewRomanB", size=12)
        pdf.cell(100, 10, txt="For: RK Arts", ln=False, align="R")
        pdf.cell(0, 10, txt="Proprietor", ln=True, align="R")  


        pdf.output(f"Invoice_{invoice_number}.pdf")
        messagebox.showinfo("Success", "Invoice exported as PDF successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

                
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
invoice_number = get_next_invoice_number()
inv_label = Label(window, text=f"Invoice No: {invoice_number}", font=("Arial", 10))
inv_label.place(x=540, y=220)

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
add_button = Button(window, text="Add Item", command=addItem)
add_button.place(x=660, y=290)

# export button
export_button = Button(window, text="Export to PDF", command=export_to_pdf)
export_button.place(x=660, y=950)

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
