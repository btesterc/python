##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
from datetime import datetime
import pandas
import smtplib
import random
MY_MAIL = "xxx"
MY_PASSWORD = "xxsdx"
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

today = (datetime.now().month, datetime.now().day)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(to_addrs=birthday_person['email'],
                            from_addr=MY_MAIL,
                            msg=f"Subject:HappyBirthday\n\n{contents}")





