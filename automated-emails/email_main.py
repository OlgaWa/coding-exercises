import yagmail
import pandas as pnd
from newsletter import NewsFeed
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


df = pnd.read_excel("mailing_list.xlsx")


def send_email():
    """Send emails with daily news on the particular topic."""
    today = str(datetime.date.today())
    yesterday = str(datetime.date.today() - datetime.timedelta(days=1))

    feed = NewsFeed(row["interest"], yesterday, today, "en")

    my_email = yagmail.SMTP(os.environ["MY_EMAIL"], os.environ["PASSWORD"])
    my_email.send(to=row["email"],
                  subject=f"Your {row['interest'].upper()} newsletter",
                  contents=f"Hi {row['name']}!\n\n"
                           f"This is your {row['interest']} "
                           f"newsletter for today:\n\n"
                           f"{feed.get()}Regards!")


for index, row in df.iterrows():
    send_email()
