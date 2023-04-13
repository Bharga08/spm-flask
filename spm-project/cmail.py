import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('bhargavasaichinni@gmail.com','avcgtspqhdztfkok')
    msg=EmailMessage()
    msg['From']='bhargavasaichinni@gmail.com'
    msg['subject']='Account Sign up OTP'
    msg['To']=to
    body=f'your one time otp for registration is{otp}'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()             
                 
    
