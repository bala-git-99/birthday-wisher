# -------------------- Extra Hard Starting Project -------------------#
import random
from mail_sender import send_email
import pandas
import datetime as dt

data = pandas.read_csv("birthdays.csv", index_col=None)
today = dt.datetime.now()
month_match = data[data.month == today.month]
day_match = data[data.day == today.day]

final_match = pandas.merge(month_match, day_match, on=["name", "email"], how="inner").to_dict("records")
birthday_names = [record["name"] for record in final_match]
birthday_emails = [record["email"] for record in final_match]
print(final_match)

if len(birthday_names) > 0:
    for name in birthday_names:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", name)
        send_email(receiver=birthday_emails[birthday_names.index(name)],
                   subject=f"Happy Birthday {name}", content=letter_content)
