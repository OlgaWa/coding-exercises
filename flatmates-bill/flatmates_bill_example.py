from flatmates_bill import Bill, Flatmate, PdfReport


# Flatmates' Bill - Command-Line Interface app.
name1 = input("Hello! What is your name? ")
amount = float(input("Please enter the bill amount (e.g. 200): "))
period = input("Please enter the bill period (e.g. March 2021): ")
days_in_the_house1 = int(input("How many days did you spend "
                               "in the house during the bill period? "))

name2 = input("What is the name of your flatmate? ")
days_in_the_house2 = int(input(f"How many days did {name2} spend in the "
                               f"house during the bill period? "))

bill1 = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_the_house1)
flatmate2 = Flatmate(name2, days_in_the_house2)

print(f"{flatmate1.name} pays: ", round(flatmate1.pays(bill1, flatmate2), 2))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(bill1, flatmate1), 2))

pdf1 = PdfReport(f"{bill1.period}")
pdf1.generate(flatmate1, flatmate2, bill1)
