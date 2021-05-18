from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html",
                               billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template("bill_form_page.html",
                               result=True,
                               billform=billform,
                               name1=flatmate1.name,
                               name2=flatmate2.name,
                               amount1=round(flatmate1.pays(the_bill, flatmate2), 2),
                               amount2=round(flatmate2.pays(the_bill, flatmate1), 2))


class BillForm(Form):

    amount = StringField("Bill amount: ")
    period = StringField("Bill period: ")

    name1 = StringField("Your name: ")
    days_in_house1 = StringField("Days in the house: ")
    name2 = StringField("Your flatmate's name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill_form", view_func=BillFormPage.as_view("bill_form_page"))

app.run(debug=True)
