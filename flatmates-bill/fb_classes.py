from fpdf import FPDF


class Bill:
    """
    Create a bill object that contains information
    about the period and total amount.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person that lives in the flat and pays the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house
                                       + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Create a pdf file that contains data about the flatmates,
    the period of the bill and how much each of them has to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pays = round(flatmate1.pays(bill, flatmate2), 2)
        flatmate2_pays = round(flatmate2.pays(bill, flatmate1), 2)

        pdf = FPDF("P", "mm", "A4")
        pdf.add_page("P")

        pdf.image("house.png", w=20, h=20)

        pdf.set_font("Arial", "B", 64)
        pdf.set_text_color(30, 0, 44)
        pdf.cell(0, 70, "Flatmates bill", 0, align="C", ln=1)

        pdf.set_font("Courier", "", 32)
        pdf.set_text_color(99, 37, 108)
        pdf.cell(0, 25, f"Period: {bill.period}", 0, align="C", ln=3)

        pdf.set_font("Arial", "B", 24)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 25, "", 0, align="C", ln=3)
        pdf.cell(100, 25, f"- {flatmate1.name}: "
                          f"{flatmate1_pays} PLN", 0, align="L", ln=1)
        pdf.cell(100, 25, f"- {flatmate2.name}: "
                          f"{flatmate2_pays} PLN", 0, align="L", ln=1)

        pdf.output(f"{self.filename}.pdf")
