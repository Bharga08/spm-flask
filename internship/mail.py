import smtplib
import random
import time
recpt=input('enter a mail')
for i in range(0,2):
    otp=random.randint(12422,99999)
#from smtplib import SMTP
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()#starts the server
server.login('206532@siddharthamahila.ac.in','klpmukzbqqpriyzt')
server.sendmail('206532@siddharthamahila.ac.in',recpt,'the otp is-'+str(otp))
server.close()
print('mail sent')
otp2=int(input('enter otp'))
if otp==otp2:
     print('the otp is valid')
else:
    print('invalid otp-check your eye sight')
