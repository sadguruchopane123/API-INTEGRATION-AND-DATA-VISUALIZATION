"""
TASK-2: Automated Report Generation
Internship: CODTECH

Description:
This script reads data from a CSV file, analyzes it,
and generates a formatted PDF report using ReportLab.
"""

import csv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ==============================
# 📂 SAMPLE DATA FILE (AUTO CREATE)
# ==============================
def create_sample_file():
    """Creates a sample CSV file"""
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks"])
        writer.writerow(["Amit", 75])
        writer.writerow(["Rahul", 85])
        writer.writerow(["Sneha", 90])
        writer.writerow(["Priya", 80])
        writer.writerow(["Karan", 70])

# ==============================
# 📊 READ AND ANALYZE DATA
# ==============================
def analyze_data():
    """Reads CSV and calculates statistics"""
    names = []
    marks = []

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            names.append(row[0])
            marks.append(int(row[1]))

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return names, marks, total, average, highest, lowest

# ==============================
# 📄 GENERATE PDF REPORT
# ==============================
def create_pdf(names, marks, total, average, highest, lowest):
    """Creates PDF report"""
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Student Marks Report", styles['Title']))
    elements.append(Spacer(1, 10))

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

    # Analysis
    elements.append(Paragraph(f"Total Marks: {total}", styles['Normal']))
    elements.append(Paragraph(f"Average Marks: {average:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Highest Marks: {highest}", styles['Normal']))
    elements.append(Paragraph(f"Lowest Marks: {lowest}", styles['Normal']))

    # Build PDF
    doc.build(elements)

# ==============================
# 🚀 MAIN FUNCTION
# ==============================
def main():
    print("Creating sample data file...")
    create_sample_file()

    print("Analyzing data...")
    names, marks, total, avg, high, low = analyze_data()

    print("Generating PDF report...")
    create_pdf(names, marks, total, avg, high, low)

    print("✅ PDF Report Generated Successfully (report.pdf)")

if __name__ == "__main__":
    main()
