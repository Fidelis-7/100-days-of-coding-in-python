# import smtplib

# my_email = "abanumfidelis7@gmail.com"
# my_password = "Felix2003!"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="abanumfidelis90@gmail.com", msg="Hello pythoneer")
#     connection.close()


# import smtplib
# import datetime as dt
# import random
#
# my_email = "abanumfidelis90@gmail.com"
# my_password = "Felix2003!"
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)


# date_of_birth = dt.datetime(year= 1995, month= 12, day= 15, hour=4, minute=30, second=49)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

my_email = "abanumfidelis90@gmail.com"
my_password = "Felix2003!"

now = dt.datetime.now()
day_of_the_week = now.weekday()
# print(day_of_the_week)
if day_of_the_week == 1:
    with open("quotes.txt", "r") as file:
        content = file.readlines()
        quote = random.choice(content)
        print(quote)
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="fidelismartin90@gmail.com",
                            msg=f"Subject: Monday motivation:\n{quote}")
        connection.close()
