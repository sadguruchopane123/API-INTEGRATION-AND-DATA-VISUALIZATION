"""
TASK-2: Automated Report Generation
Internship: CODTECH

Description:
This script reads data from a CSV file, analyzes it,
and generates a formatted PDF report using ReportLab.
It calculates total, average, highest, and lowest values.
"""

import csv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ==============================
# 📂 CREATE SAMPLE DATA FILE
# ==============================
def create_sample_data():
    print("Creating sample data file...")

    with open("student_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks"])

        writer.writerow(["Amit", 78])
        writer.writerow(["Rahul", 85])
        writer.writerow(["Sneha", 92])
        writer.writerow(["Priya", 88])
        writer.writerow(["Karan", 73])

    print("✅ Sample data file created: student_data.csv")

# ==============================
# 📊 READ AND ANALYZE DATA
# ==============================
def analyze_data():
    print("Analyzing data...")

    names = []
    marks = []

    with open("student_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            names.append(row[0])
            marks.append(int(row[1]))

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("✅ Data analysis completed")

    return names, marks, total, average, highest, lowest

# ==============================
# 📄 GENERATE PDF REPORT
# ==============================
def generate_pdf(names, marks, total, avg, high, low):
    print("Generating PDF report...")

    doc = SimpleDocTemplate("student_report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Student Marks Report", styles['Title']))
    elements.append(Spacer(1, 15))

    # Table Data
    table_data = [["Name", "Marks"]]
    for i in range(len(names)):
        table_data.append([names[i], marks[i]])

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # Analysis Section
    elements.append(Paragraph(f"Total Marks: {total}", styles['Normal']))
    elements.append(Paragraph(f"Average Marks: {avg:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Highest Marks: {high}", styles['Normal']))
    elements.append(Paragraph(f"Lowest Marks: {low}", styles['Normal']))

    # Build PDF
    doc.build(elements)

    print("✅ PDF Generated: student_report.pdf")

# ==============================
# 🚀 MAIN FUNCTION
# ==============================
def main():
    create_sample_data()
    names, marks, total, avg, high, low = analyze_data()
    generate_pdf(names, marks, total, avg, high, low)

    print("🎉 Task-2 Completed Successfully!")

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    main()
