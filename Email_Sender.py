##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import pandas
import random 




now=dt.datetime.now()
year=now.year
today_bd=(now.month,now.day)


#-----birthday_CSV checking-----#

data_csv=pandas.read_csv("./Desktop/birthdays.csv")
birthday_dic={(data_row["month"],data_row["day"]):data_row for index, data_row in data_csv.iterrows()}

if today_bd in birthday_dic:
    bd_person=birthday_dic[today_bd]
    
    file_path=f"./Desktop/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=file_path,) as letter:
        contents=letter.read()
        contents = contents.replace("[NAME]",bd_person["name"])

    EMAIL="rakshitv7979@gmail.com"
    PASSWORD="bsna pbxp bnee luao"

    connection=smtplib.SMTP("smtp.gmail.com" , port=587)
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)

    connection.sendmail(from_addr=EMAIL,to_addrs=bd_person["email"],msg=f"Subject: Happy Birthday\n\n Hello {contents}")
    connection.close
