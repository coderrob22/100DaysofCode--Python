import smtplib
import datetime as dt
import random

my_email = 'app.production02@gmail.com'
my_password = 'ksigssggokzhrzmf'

    
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()

        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f'Subject:Quote of the day! \n\n {random_quote}.'
            )
