import tkinter as tk
from tkinter import ttk
from validation import validate_date, validate_email, EntryWithLimit

def create_students_window(main_window):
    window = tk.Toplevel(main_window)
    window.geometry("850x850")
    window.title("Students Table")
    window.configure(bg="white")

    def on_close():
        window.destroy()
        main_window.deiconify()

    window.protocol("WM_DELETE_WINDOW", on_close)

    heading = tk.Label(window, text="Students Table", font=("Georgia", 24),
                     fg="sky blue", bg="white")
    heading.pack(padx=20, pady=20)

    labelWidth = 20

    def field(text, fieldType="text"):
        frame = tk.Frame(window, bg="white")
        frame.pack(fill="x", pady=5)

        label = tk.Label(frame, text=text, font=("Georgia", 14),
                       fg="#ff4d00", bg="white", width=labelWidth, anchor="w")
        label.pack(side="left", padx=5, pady=5)

        if fieldType == "dropdown":
            dropDown = ttk.Combobox(frame, font=("Arial", 16), values=["Yes", "No"],
                                 state="readonly", width=18)
            dropDown.set("Yes")
            dropDown.pack(side="left", padx=5)
            return dropDown

        elif fieldType == "email":
            entry = ttk.Entry(frame, width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            return entry, error_label

        elif fieldType == "date":
            entry = ttk.Entry(frame, width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            return entry, error_label

        elif fieldType == "phone":
            entry = EntryWithLimit(frame, max_length=10, fieldType="numeric",
                                 width=25, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label

        elif fieldType == "age":
            entry = EntryWithLimit(frame, max_length=2, fieldType="numeric",
                                 width=10, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label

        elif fieldType == "name":
            entry = EntryWithLimit(frame, max_length=25, fieldType="text",
                                 width=20, font=("Arial", 16))
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
        dobValue = dob.get()
        enrollValue = enrollment_date.get()
        email_value = email.get().strip()
        age_value = age.get()
        phone_value = phone.get()

        # Reset errors
        dob_error.config(text="")
        enroll_error.config(text="")
        phone_error.config(text="")
        email_error.config(text="")
        first_error.config(text="")
        last_error.config(text="")
        parents_error.config(text="")
        address_error.config(text="")
        age_error.config(text="")

        is_valid = True

        #validate first name
        if not firstName.get().strip():
            first_error.config(text="First name required")
            is_valid = False

        #validate last name
        if not lastName.get().strip():
            last_error.config(text="Last name required")
            is_valid = False

        #validate parents' name
        if not parentsName.get().strip():
            parents_error.config(text="Parents full name required")
            is_valid = False

        #validate address
        if not address.get().strip():
            address_error.config(text="Address required")
            is_valid = False

        #validate age
        if not age_value:
            age_error.config(text="Age required")
            is_valid = False

        #validate dob
        if not validate_date(dobValue):
            dob_error.config(text="Invalid date (MM/DD/YYYY)")
            is_valid = False
        elif dobValue == enrollValue:
            dob_error.config(text="Cannot match Enrollment Date")
            is_valid = False

        #enrollment date
        if not validate_date(enrollValue):
            enroll_error.config(text="Invalid date (MM/DD/YYYY)")
            is_valid = False
        elif enrollValue == dobValue:
            enroll_error.config(text="Cannot match Date of Birth")
            is_valid = False

        #phone
        if len(phone_value) != 10 or not phone_value.isdigit():
            phone_error.config(text="Phone must be 10 digits")
            is_valid = False

        #email
        if not email_value:
            email_error.config(text="Email required")
            is_valid = False
        elif not validate_email(email_value):
            email_error.config(text="Email must end with @gmail.com")
            is_valid = False

        if is_valid:
            success_label = tk.Label(window, text="Form submitted successfully!",
                                   fg="green", font=("Arial", 12))
            success_label.pack(pady=10)

    #create all fields
    firstName, first_error = field("Enter First Name:", "name")
    lastName, last_error = field("Enter Last Name:", "name")
    age, age_error = field("Enter Age:", "age")
    parentsName, parents_error = field("Enter Parents Full Name:", "name")
    email, email_error = field("Enter Email:", "email")
    dob, dob_error = field("Enter Date of Birth:\nMM/DD/YY", "date")
    enrollment_date, enroll_error = field("Enter Enrollment Date:\nMM/DD/YY", "date")
    address, address_error = field("Enter Address:", "name")
    enrollmentStatus = field("Enrollment Status:", "dropdown")
    phone, phone_error = field("Enter Phone Number:", "phone")

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