import tkinter as tk
from tkinter import ttk
from validation import validate_date, EntryWithLimit

def create_teachers_payments_window(main_window):
    window = tk.Toplevel(main_window)
    window.geometry("750x800")
    window.title("Teachers Payments")
    window.configure(bg="white")

    def on_close():
        window.destroy()
        main_window.deiconify()

    window.protocol("WM_DELETE_WINDOW", on_close)

    #create header
    heading = tk.Label(window, text="Teachers Payments", font=("Georgia", 18), 
                     bg="white", fg="sky blue")
    heading.pack(padx=20, pady=20)

    labelWidth = 20

    def field(text, fieldType="text"): 
        frame = tk.Frame(window, bg="white")
        frame.pack(anchor="w", pady=5)

        label = tk.Label(frame, text=text, font=("Georgia", 16), 
                       bg="white", fg="#ff4d00", width=labelWidth, anchor="w")
        label.pack(side="left", padx=5, pady=5, anchor="w")
        
        if fieldType == "date":
            entry = ttk.Entry(frame, width=20, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            return entry, error_label
        
        elif fieldType == "amount":
            entry = EntryWithLimit(frame, max_length=6,
                                 width=20, font=("Arial", 16), fieldType="numeric") 
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label  
            return entry, error_label

        elif fieldType == "dropdown1":
            dropDown = ttk.Combobox(frame, font=("Arial", 16), 
                                  values=["Complete", "Pending"], 
                                  state="readonly", width=18)
            dropDown.set("Complete")
            dropDown.pack(side="left", padx=5)
            return dropDown
        
        elif fieldType == "dropdown2":
            dropDown = ttk.Combobox(frame, font=("Arial", 16), 
                                  values=["Credit Card", "Bank Transfer", "Cash", "Other"], 
                                  state="readonly", width=18)
            dropDown.set("Credit Card")
            dropDown.pack(side="left", padx=5)
            return dropDown
        
        elif fieldType == "name": 
            entry = EntryWithLimit(frame, max_length=20, fieldType="text", 
                                 width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label
        
        else:
            entry = ttk.Entry(frame, width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            return entry
        
    def on_submit():
        #reset all error messages
        teacherName_error.config(text="")
        paymentDate_error.config(text="")
        amount_error.config(text="")
        
        is_valid = True

        #teacher name validation
        if not teacherName.get().strip():
            teacherName_error.config(text="Teacher Name required")
            is_valid = False

        #payment date validation
        date_valid = validate_date(paymentDate.get())
        if not date_valid:
            paymentDate_error.config(text="Invalid date (MM/DD/YYYY)")
            is_valid = False

        #amount validation
        if not amount.get():
            amount_error.config(text="Amount required")
            is_valid = False
        elif not amount.get().isdigit():
            amount_error.config(text="Numbers only")
            is_valid = False

        if is_valid:
            success_label = tk.Label(window, text="Form submitted successfully!", 
                                   fg="green", font=("Arial", 12))
            success_label.pack(pady=10)

    #create all fields
    teacherName, teacherName_error = field("Enter Teacher Name:", "name")
    paymentDate, paymentDate_error = field("Enter Payment Date\nMM/DD/YY:", "date")
    amount, amount_error = field("Enter Amount:($)", "amount")
    paymentMethod = field("Enter Payment Method", "dropdown2")
    status = field("Enter Status:", "dropdown1") 

    #submit button
    submitButton = tk.Button(window, text="Submit", bg="dark blue", 
                           fg="white", font=("Georgia", 18), 
                           width=6, height=1, command=on_submit)
    submitButton.pack(pady=20)

    #back button
    back_button = tk.Button(window, text="Back to Menu", bg="gray",
                          fg="white", font=("Georgia", 12),
                          command=on_close)
    back_button.pack(pady=10)