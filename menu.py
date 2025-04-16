import tkinter as tk
from students_table import create_students_window
from bookstable import create_books_window
from teachers_payments import create_teachers_payments_window
from teachers_invoice import create_teachers_invoice_window
from curriculum import create_curriculum_window

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("700x650")
        self.root.configure(bg="white")
        
        self.create_widgets()
    
    def create_widgets(self):
        heading = tk.Label(self.root, text="Main Menu", 
                         font=("Georgia", 24), fg="sky blue", bg="white")
        heading.pack(pady=20)

        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(expand=True)

        button_style = {
            "font": ("Georgia", 14),
            "width": 20,
            "height": 2,
            "bg": "bisque",
            "fg": "black",
            "bd": 0
        }

        students_btn = tk.Button(button_frame, text="Students Table", 
                               command=self.open_students, **button_style)
        students_btn.pack(pady=5)

        books_btn = tk.Button(button_frame, text="Books Table",
                            command=self.open_books, **button_style)
        books_btn.pack(pady=5)

        teachersP_btn = tk.Button(button_frame, text="Teachers Payments",
                        command=self.open_teachers_payments, **button_style)
        teachersP_btn.pack(pady=5)

        teachersI_btn = tk.Button(button_frame, text="Teachers Invoice",
                        command=self.open_teachers_invoice, **button_style)
        teachersI_btn.pack(pady=5)

        curriculum_btn = tk.Button(button_frame, text="Curriculum Table",
                         command=self.open_curriculum, **button_style)
        curriculum_btn.pack(pady=5)

        exit_btn = tk.Button(button_frame, text="Exit", 
                           command=self.root.destroy, **button_style)
        exit_btn.pack(pady=5)
    
    def open_students(self):
        self.root.withdraw()
        create_students_window(self.root)
    
    def open_books(self):
        self.root.withdraw()
        create_books_window(self.root)

    def open_teachers_payments(self):
        self.root.withdraw()
        create_teachers_payments_window(self.root)

    def open_teachers_invoice(self):
        self.root.withdraw()
        create_teachers_invoice_window(self.root)

    def open_curriculum(self):
        self.root.withdraw()
        create_curriculum_window(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()