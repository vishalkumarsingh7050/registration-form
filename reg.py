import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

def generate_qr():
    name = entry_name.get()
    PRN = entry_PRN.get()
    phone = entry_phone.get()
    Hostels = Hostels_var.get()
    Cateogries= Cateogries_var.get()

    if name == "" or PRN == "" or phone == "" or Hostels == "Select Course" or Cateogries == "select cateogries":
        messagebox.showerror("Error", "All fields are required!")
        return

    # ----------- UPI PAYMENT DETAILS -----------
    upi_id = "vishal.ayan7050@okicici"       # change to your UPI ID
    payee_name = "Vishal kumar singh"       # change to your name
    amount = "10"                 # amount you want to receive
    # -------------------------------------------

    upi_link = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR"

    # Generate QR
    qr = qrcode.make(upi_link)
    qr.save("qr.png")

    img = Image.open("qr.png")
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)

    qr_label.config(image=photo)
    qr_label.image = photo

    messagebox.showinfo("QR Generated", 
                        f"Scan this QR to Pay ₹{amount}\nAfter payment, click Submit!")

def submit_form():
    messagebox.showinfo("Success", "Registration Completed!\nPayment Verified!")

# GUI Window
root = tk.Tk()
root.title("H P L 2K25🏏🏏🏏⚾")
root.geometry("420x650")
root.config(bg="lightyellow")

tk.Label(root, text="Registration form of HPL🏏🏏", font=("Arial", 18, "bold"), bg="lightyellow").pack(pady=10)

# Name
tk.Label(root, text="Full Name:", bg="lightyellow").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

# PRN
tk.Label(root, text="PRN:", bg="lightyellow").pack()
entry_PRN = tk.Entry(root, width=40)
entry_PRN.pack(pady=5)

# Phone
tk.Label(root, text="Phone:", bg="lightyellow").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack(pady=5)

# Hostels
tk.Label(root, text="Select Hostels:", bg="lightyellow").pack()
Hostels_var = tk.StringVar()
Hostels_var.set("Select Hostels")

Hostels = ["B4", "B5", "B1", "SQ"]
tk.OptionMenu(root, Hostels_var, *Hostels).pack(pady=5)

#CATEOGRIES

tk.Label(root, text="Select Cateogries:", bg="lightyellow").pack()
Cateogries_var = tk.StringVar()
Cateogries_var.set("Select Cateogries")

Cateogries = ["WK", "Bowller", "BAtter", "ALL rounder"]
tk.OptionMenu(root, Cateogries_var, *Cateogries).pack(pady=5)
# QR Image Label
qr_label = tk.Label(root, bg="lightyellow")
qr_label.pack(pady=10)

# Buttons
tk.Button(root, text="Generate UPI QR", command=generate_qr, bg="blue", fg="white",
          font=("Arial", 12), width=20).pack(pady=10)

tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white",
          font=("Arial", 12), width=20).pack(pady=10)

root.mainloop()
