import tkinter as tk
from tkinter import ttk
from validation import EntryWithLimit

def create_curriculum_window(main_window):
    window = tk.Toplevel(main_window)
    window.geometry("750x800")
    window.title("Curriculum Table")
    window.configure(bg="white")

    def on_close():
        window.destroy()
        main_window.deiconify()

    window.protocol("WM_DELETE_WINDOW", on_close)


    heading = tk.Label(window, text="Curriculum Table", font=("Georgia", 18), 
                     bg="white", fg="sky blue")
    heading.pack(padx=20, pady=20)

    labelWidth = 20

    def field(text, fieldType="text"): 
        frame = tk.Frame(window, bg="white")
        frame.pack(anchor="w", pady=5)

        label = tk.Label(frame, text=text, font=("Georgia", 16), 
                       bg="white", fg="#ff4d00", width=labelWidth, anchor="w")
        label.pack(side="left", padx=5, pady=5, anchor="w")
        
        if fieldType == "integer":
            entry = EntryWithLimit(frame, max_length=2, fieldType="integer",
                                width=20, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label
        else:
            entry = EntryWithLimit(frame, max_length=20, fieldType="text",
                                width=20, font=("Arial", 16))
            entry.pack(side="left", padx=5)
            error_label = tk.Label(frame, text="", fg="red", bg="white", font=("Arial", 10))
            error_label.pack(side="bottom", anchor="w")
            entry.error_label = error_label
            return entry, error_label

    def on_submit():

        gradeLevel_error.config(text="")
        courseName_error.config(text="")
        courseDescription_error.config(text="")
        
        is_valid = True

        if not gradeLevel.get().strip():
            gradeLevel_error.config(text="Grade level required")
            is_valid = False
        elif not gradeLevel.get().isdigit():
            gradeLevel_error.config(text="Must be a number")
            is_valid = False

 
        if not courseName.get().strip():
            courseName_error.config(text="Course name required")
            is_valid = False

 
        if not courseDescription.get().strip():
            courseDescription_error.config(text="Description required")
            is_valid = False

        if is_valid:
            success_label = tk.Label(window, text="Form submitted successfully!", 
                                   fg="green", font=("Arial", 12))
            success_label.pack(pady=10)
            window.after(3000, success_label.destroy)


    gradeLevel, gradeLevel_error = field("Enter Grade Level:", "integer")
    courseName, courseName_error = field("Enter Course Name:")
    courseDescription, courseDescription_error = field("Enter Course Description:")


    submitButton = tk.Button(window, text="Submit", bg="dark blue", 
                           fg="white", font=("Georgia", 18), 
                           width=6, height=1, command=on_submit)
    submitButton.pack(pady=20)


    back_button = tk.Button(window, text="Back to Menu", bg="gray",
                          fg="white", font=("Georgia", 12),
                          command=on_close)
    back_button.pack(pady=10)