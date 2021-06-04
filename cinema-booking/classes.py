import random
import string
import mysql.connector
import os
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            if card.validate(seat.get_price()):
                seat.occupy()
                ticket = Ticket(self, seat.get_price, seat.seat_id)
                ticket.to_pdf()
                return "Purchase successful"
            else:
                return "There was a problem with your card!"
        else:
            return "That seat is taken!"


class Seat:

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        db = mysql.connector.connect(
            host="localhost",
            user=os.environ["USER"],
            password=os.environ["DB_PASSWORD"],
            database="cinema")
        cursor = db.cursor()
        cursor.execute("SELECT price from seat WHERE seat_id=%s",
                       (self.seat_id, ))
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        db = mysql.connector.connect(
            host="localhost",
            user=os.environ["USER"],
            password=os.environ["DB_PASSWORD"],
            database="cinema")
        cursor = db.cursor()
        query = "SELECT taken FROM seat WHERE seat_id = %s"
        this_seat = (self.seat_id, )
        cursor.execute(query, this_seat)
        taken = cursor.fetchall()[0][0]
        if taken == 0:
            return True
        else:
            return False

    def occupy(self):
        db = mysql.connector.connect(
            host="localhost",
            user=os.environ["USER"],
            password=os.environ["DB_PASSWORD"],
            database="cinema")
        cursor = db.cursor()
        cursor.execute("UPDATE seat SET taken=%s WHERE seat_id=%s",
                       (1, self.seat_id, ))
        db.commit()
        db.close()


class Card:

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        db = mysql.connector.connect(
            host="localhost",
            user=os.environ["USER"],
            password=os.environ["DB_PASSWORD"],
            database="banking")
        cursor = db.cursor()
        cursor.execute("SELECT balance from card WHERE number=%s and cvc=%s",
                       (self.number, self.cvc, ))
        result = cursor.fetchall()
        if result:
            balance = result[0][0]
            if balance >= price:
                cursor.execute("UPDATE card SET balance=%s "
                               "WHERE number=%s and cvc=%s",
                               (balance-price, self.number, self.cvc, ))
                db.commit()
                db.close()
                return True


class Ticket:

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters)
                           for i in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):

        pdf = FPDF("P", "mm", "A4")
        pdf.add_page("P")

        pdf.set_font("Arial", "B", 64)
        pdf.set_text_color(30, 0, 44)
        pdf.cell(0, 70, "Your ticket", 0, align="C", ln=1)

        pdf.set_font("Courier", "", 32)
        pdf.set_text_color(99, 37, 108)
        pdf.cell(0, 25, self.user.name, 0, align="C", ln=3)
        pdf.cell(0, 25, self.id, 0, align="C", ln=3)

        pdf.set_font("Arial", "B", 24)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 25, f"Seat number: {self.seat_number}", 0,
                 align="C", ln=1)

        pdf.output("ticket.pdf")
