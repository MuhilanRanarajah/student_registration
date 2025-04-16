import tkinter as tk
from tkinter import ttk

#validate date
def validate_date(date_str):
    dateList = date_str.split('/')
    
    if len(dateList) == 3:
        year = dateList[0] #2025
        month = dateList[1] #12
        day = dateList[2] #22
    
    if not (dateList[0].isdigit() and dateList[1].isdigit() and dateList[2].isdigit()):
        return False
    
    month, day, year = map(int, dateList)
    
    valid_month = 1 <= month <= 12
    valid_day = 1 <= day <= 31
    valid_year = 1900 <= year <= 2100
    
    return valid_month and valid_day and valid_year

#validate email
def validate_email(email):
    return email.strip().lower().endswith("@gmail.com")

#validate phone
class EntryWithLimit(ttk.Entry):
    def __init__(self, master, max_length, fieldType="text", **kw):
        super().__init__(master, **kw)
        self.max_length = max_length
        self.fieldType = fieldType
        text_checker = master.register(self.validInput)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))
        self.error_label = None

    def validInput(self, text):
        if len(text) > self.max_length:
            if self.error_label:
                self.error_label.config(text=f"Max {self.max_length} digits")
            return False
        if self.fieldType == "numeric" and text and not text.isdigit():
            if self.error_label:
                self.error_label.config(text="Numbers only")
            return False
        if self.fieldType == "phone" and len(text) == self.max_length:
            if self.error_label:
                self.error_label.config(text="")
            return True 
        elif self.fieldType == "phone" and 0 < len(text) < self.max_length:
            if self.error_label:
                self.error_label.config(text=f"Must be exactly {self.max_length} digits")
            return True
        if self.error_label:
            self.error_label.config(text="")
        return True