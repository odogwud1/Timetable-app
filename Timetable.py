from fpdf import FPDF
import os

def get_unique_filename(base_name):
    name, ext = os.path.splitext(base_name)
    counter = 1
    while os.path.exists(base_name):
        base_name = f"{name} ({counter}){ext}"
        counter += 1
    return base_name

days = {
    "Monday": [
        ("6:15-6:30 AM", "Wake up, hygiene"),
        ("6:30-7:00 AM", "Workout"),
        ("7:00-8:30 AM", "Prayers"),
        ("8:30-9:00 AM", "Light Breakfast"),
        ("9:00-12:30 PM", "Work"),
        ("12:30-1:30 PM", "Lunch + Short Break"),
        ("1:30-5:30 PM", "Work"),
        ("5:30-6:30 PM", "Light activity / Rest"),
        ("6:30-7:30 PM", "Dinner"),
        ("7:30-8:00 PM", "Relax / Social"),
        ("8:00-9:30 PM", "Study"),
        ("9:30-10:30 PM", "Self-Development / Side Project"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Tuesday": [
        ("6:15-6:30 AM", "Wake up, hygiene"),
        ("6:30-7:00 AM", "Workout"),
        ("7:00-8:30 AM", "Prayers"),
        ("8:30-9:00 AM", "Light Breakfast"),
        ("9:00-12:30 PM", "Work"),
        ("12:30-1:30 PM", "Lunch + Short Break"),
        ("1:30-5:30 PM", "Work"),
        ("5:30-6:30 PM", "Light activity / Rest"),
        ("6:30-7:30 PM", "Dinner"),
        ("7:30-8:00 PM", "Relax / Social"),
        ("8:00-9:30 PM", "Study"),
        ("9:30-10:30 PM", "Self-Development / Side Project"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Wednesday": [
        ("6:15-6:30 AM", "Wake up, hygiene"),
        ("6:30-7:00 AM", "Workout"),
        ("7:00-8:30 AM", "Prayers"),
        ("8:30-9:00 AM", "Light Breakfast"),
        ("9:00-12:30 PM", "Work"),
        ("12:30-1:30 PM", "Lunch + Short Break"),
        ("1:30-5:30 PM", "Work"),
        ("5:30-6:30 PM", "Light activity / Rest"),
        ("6:30-7:30 PM", "Dinner"),
        ("7:30-8:00 PM", "Relax / Social"),
        ("8:00-9:30 PM", "Study"),
        ("9:30-10:30 PM", "Self-Development / Side Project"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Thursday": [
        ("6:15-6:30 AM", "Wake up, hygiene"),
        ("6:30-7:00 AM", "Workout"),
        ("7:00-8:30 AM", "Prayers"),
        ("8:30-9:00 AM", "Light Breakfast"),
        ("9:00-12:30 PM", "Work"),
        ("12:30-1:30 PM", "Lunch + Short Break"),
        ("1:30-5:30 PM", "Work"),
        ("5:30-6:30 PM", "Light activity / Rest"),
        ("6:30-7:30 PM", "Dinner"),
        ("7:30-8:00 PM", "Relax / Social"),
        ("8:00-9:30 PM", "Study"),
        ("9:30-10:30 PM", "Self-Development / Side Project"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Friday": [
        ("6:15-6:30 AM", "Wake up, hygiene"),
        ("6:30-7:00 AM", "Workout"),
        ("7:00-8:30 AM", "Prayers"),
        ("8:30-9:00 AM", "Light Breakfast"),
        ("9:00-12:30 PM", "Work"),
        ("12:30-1:30 PM", "Lunch"),
        ("1:30-5:00 PM", "Work"),
        ("5:30-7:30 PM", "Football"),
        ("7:30-8:30 PM", "Dinner + Shower"),
        ("8:30-9:30 PM", "Study"),
        ("9:30-10:30 PM", "Self-Development"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Saturday": [
        ("8:15-8:30 AM", "Wake up, hygiene"),
        ("8:30-9:00 AM", "Prayers"),
        ("9:00-10:00 AM", "Additional Workout"),
        ("10:30 AM-1:00PM", "Study"),
        ("1:30-1:30 PM", "Lunch"),
        ("1:30-5:00 PM", "Free Time"),
        ("5:30-7:30 PM", "Football"),
        ("7:30-8:30 PM", "Dinner + Shower"),
        ("8:30-9:30 PM", "Self-Development"),
        ("9:30-10:30 PM", "Relax / Social"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ],
    "Sunday": [
        ("6:50-8:30 AM", "Wake up, hygiene")
        ("8:30-12:30 PM", "Church"),
        ("12:30-1:30 PM", "Lunch"),
        ("1:30-5:00 PM", "Free Time"),
        ("5:30-7:30 PM", "Football"),
        ("7:30-8:30 PM", "Dinner + Shower"),
        ("8:30-9:30 PM", "Self-Development"),
        ("9:30-10:30 PM", "Relax / Social"),
        ("10:30-11:00 PM", "Wind-down & hygiene"),
        ("11:00 PM-6:15 AM", "Sleep")
    ]
}


pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for day, schedule in updated_days.items():
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"{day} Schedule", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Time", border=1)
    pdf.cell(130, 10, "Activity", border=1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for time, activity in schedule:
        pdf.cell(60, 10, time, border=1)
        pdf.cell(130, 10, activity, border=1)
        pdf.ln()

# Save the PDF

final_pdf_name = get_unique_filename("Weekly_Timetable.pdf")
pdf.output(final_pdf_name)
print(f"PDF saved as {final_pdf_name}")

