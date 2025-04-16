import tkinter as tk
from tkinter import ttk
from validation import validate_date, EntryWithLimit

def create_teachers_invoice_window(main_window):
    window = tk.Toplevel(main_window)
    window.geometry("750x800")
    window.title("Teachers Invoice")
    window.configure(bg="white")

    def on_close():
        window.destroy()
        main_window.deiconify()

    window.protocol("WM_DELETE_WINDOW", on_close)


    heading = tk.Label(window, text="Teachers Invoice", font=("Georgia", 18), 
                     bg="white", fg="sky blue")
    heading.pack(padx=20, pady=20)

    labelWidth = 20

    def field(text, fieldType="text"):
        frame = tk.Frame(window, bg="white")
        frame.pack(fill="x", pady=5)

        label = tk.Label(frame, text=text, font=("Georgia", 14), bg="white", 
                       fg="#ff4d00", width=labelWidth, anchor="w")
        label.pack(side="left", padx=5, pady=5)

        if fieldType == "date":
            entry = ttk.Entry(frame, width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            return entry, error_label
        
        elif fieldType == "amount":
            entry = EntryWithLimit(frame, max_length=6, fieldType="numeric",
                                width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label
        
        elif fieldType == "name":
            entry = EntryWithLimit(frame, max_length=25, fieldType="text", 
                               width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label

        elif fieldType == "dropdown":
            dropDown = ttk.Combobox(frame, font=("Arial", 16), 
                                  values=["Credit Card", "Bank Transfer", "Cash"], 
                                  state="readonly", width=23)
            dropDown.set("Payment Method")
            dropDown.pack(side="left", padx=5)
            return dropDown

        else:
            entry = ttk.Entry(frame, width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            return entry

    def on_submit():

        payment_date_error.config(text="")
        amount_error.config(text="")
        teacher_error.config(text="")

        is_valid = True

        if not validate_date(payment_date.get()):
            payment_date_error.config(text="Invalid date (MM/DD/YYYY)")
            is_valid = False

        amount_value = amount.get()
        if not amount_value:
            amount_error.config(text="Amount required")
            is_valid = False
        elif not amount_value.isdigit():
            amount_error.config(text="Must be a number")
            is_valid = False

        if not teacher_name.get().strip():
            teacher_error.config(text="Teacher name required")
            is_valid = False

        if is_valid:
            success_label = tk.Label(window, text="Invoice submitted successfully!", 
                                   fg="green", font=("Arial", 12))
            success_label.pack(pady=10)


    teacher_name, teacher_error = field("Teacher Name:", "name")
    payment_date, payment_date_error = field("Payment Date \n(MM/DD/YYYY):", "date")
    amount, amount_error = field("Amount ($):", "amount")
    payment_method = field("Payment Method:", "dropdown")


    submitButton = tk.Button(window, text="Submit", bg="dark blue", 
                           fg="white", font=("Georgia", 18), 
                           width=6, height=1, command=on_submit)
    submitButton.pack(pady=20)


    back_button = tk.Button(window, text="Back to Menu", bg="gray",
                          fg="white", font=("Georgia", 12),
                          command=on_close)
    back_button.pack(pady=10)