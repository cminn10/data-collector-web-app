from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, num_in):
    #Type in your sending email address and password
    #The smtplib setting is for gmail only
    from_email = "xxx@xxxx.xxx" 
    from_pw = "xxxxxx"
    to_email = email

    subject = "Height Data as Requested"
    message = "Here is your height data: <strong>{0}</strong> cm. Average height of all is <strong>{1}</strong> cm (Calculated out of <strong>{2}</strong> participants).</br>Thanks for your participation!".format(height, average_height, num_in)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pw)
    gmail.send_message(msg)