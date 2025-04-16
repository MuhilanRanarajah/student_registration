import tkinter as tk
from tkinter import ttk
from validation import validate_date, EntryWithLimit

def create_books_window(main_window):
    window = tk.Toplevel(main_window)
    window.geometry("750x800")
    window.title("Bookstable")
    window.configure(bg="white")

    def on_close():
        window.destroy()
        main_window.deiconify()

    window.protocol("WM_DELETE_WINDOW", on_close)

    heading = tk.Label(window, text="Bookstable", font=("Georgia", 18), 
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
        
        elif fieldType == "cost":
            entry = EntryWithLimit(frame, max_length=6, fieldType="numeric",
                                 width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label
        
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
        #reset error messages
        dob_error.config(text="")
        cost_error.config(text="")
        buyer_error.config(text="")
        title_error.config(text="")

        is_valid = True

        if not validate_date(dob.get()):
            dob_error.config(text="Invalid date (MM/DD/YYYY)")
            is_valid = False

        cost_value = cost.get()
        if not cost_value:
            cost_error.config(text="Cost required")
            is_valid = False
        elif not cost_value.isdigit():
            cost_error.config(text="Must be a number")
            is_valid = False

        if not buyerName.get().strip():
            buyer_error.config(text="Name required")
            is_valid = False

        if not bookTitle.get().strip():
            title_error.config(text="Book Title required")
            is_valid = False

        if is_valid:
            success_label = tk.Label(window, 
                                   text="Book record submitted successfully!", 
                                   fg="green", font=("Arial", 12))
            success_label.pack(pady=10)

    #create all fields
    buyerName, buyer_error = field("Enter Buyer Name:", "name")
    bookTitle, title_error = field("Enter Book Title:", "name")
    cost, cost_error = field("Enter Cost ($):", "cost")
    dob, dob_error = field("Enter Sale Date \n(MM/DD/YYYY):", "date")

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