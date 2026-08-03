import smtplib
import datetime as dt
import random
import pandas as pd
import os

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today_tuple = (today_month, today_day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

letter_options = ["/letter_templates/letter_1.txt",
				  "/letter_templates/letter_2.txt",
				  "/letter_templates/letter_3.txt"]

if today_tuple in birthdays_dict:
	birthday_person = birthdays_dict[today_tuple]

	chosen_file = random.choice(letter_options)

	with open(chosen_file) as letter_file:
		letter_contents = letter_file.read()

		final_letter = letter_contents.replace("[NAME]",birthday_person["name"])

	my_email = os.environ.get("MY_EMAIL")
	my_password = os.environ.get("MY_PASSWORD")

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=my_password)

		# Sends email.
		connection. sendmail(
			from_addr=my_email,
			to_addrs=birthday_person["email"],
			msg=f"Subject:Happy Birthday!\n\n{final_letter}."
		)
