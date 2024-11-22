import tkinter as tk
from tkinter import messagebox

class Student:
    def _init_(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = self.calculate_percentage()
        self.grade = self.assign_grade()
       
    def calculate_percentage(self):
        total_possible_marks = len(self.marks) * 100  # Assuming each subject is out of 100
        return (self.total_marks / total_possible_marks) * 100
   
    def assign_grade(self):
        percentage = self.percentage
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C+'
        elif percentage >= 40:
            return 'C'
        else:
            return 'F'

    def get_result(self):
        return (f"Student Name: {self.name}\n"
                f"Roll Number: {self.roll_number}\n"
                f"Marks: {self.marks}\n"
                f"Total Marks: {self.total_marks}\n"
                f"Percentage: {self.percentage:.2f}%\n"
                f"Grade: {self.grade}")
