from fpdf import FPDF
from filestack import Client
import os
from dotenv import load_dotenv

load_dotenv()


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

        # Add image.
        pdf.image("files/house.png", w=20, h=20)

        # Insert title.
        pdf.set_font("Arial", "B", 64)
        pdf.set_text_color(30, 0, 44)
        pdf.cell(0, 70, "Flatmates' bill", 0, align="C", ln=1)

        # Insert period of the bill.
        pdf.set_font("Courier", "", 32)
        pdf.set_text_color(99, 37, 108)
        pdf.cell(0, 25, f"Period: {bill.period}", 0, align="C", ln=3)

        # Insert names and due amounts of both flatmates.
        pdf.set_font("Arial", "B", 24)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 25, "", 0, align="C", ln=3)
        pdf.cell(100, 25, f"- {flatmate1.name}: "
                          f"{flatmate1_pays} PLN", 0, align="L", ln=1)
        pdf.cell(100, 25, f"- {flatmate2.name}: "
                          f"{flatmate2_pays} PLN", 0, align="L", ln=1)

        os.chdir("files")
        pdf.output(self.filename)


class FileSharer:

    def __init__(self, filepath, api_key=os.environ["FILESTACK_API_KEY"]):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
