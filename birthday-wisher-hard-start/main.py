##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

import datetime as dt
import smtplib
import random
import pandas

my_email = 'app.production02@gmail.com'
my_password = 'ksigssggokzhrzmf'

now = dt.datetime.now()
month = now.month
date = now.day
today = (month, date)

data = pandas.read_csv('birthdays.csv')


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
    with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthday_person['name'])

    
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
          connection.starttls()
          connection.login(my_email, my_password)
          connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person['email'],
                msg=f'Subject:Birthday Greetings\n\n{content}'
          )