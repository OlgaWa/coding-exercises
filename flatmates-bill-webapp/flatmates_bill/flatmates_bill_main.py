from flat import Bill, Flatmate
from reports import PdfReport, FileSharer


name1 = input("Hello! What is your name? ")
amount = float(input("Please enter the bill amount (e.g. 200): "))
period = input("Please enter the bill period (e.g. March 2021): ")
days_in_the_house1 = int(input("How many days did you spend in the house during the bill period? "))

name2 = input("What is the name of your flatmate? ")
days_in_the_house2 = int(input(f"How many days did {name2} spend in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_the_house1)
flatmate2 = Flatmate(name2, days_in_the_house2)

print(f"{flatmate1.name} pays: ", round(flatmate1.pays(the_bill, flatmate2), 2))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(the_bill, flatmate1), 2))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)


file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
