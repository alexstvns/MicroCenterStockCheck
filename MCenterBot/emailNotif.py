from email.mime.nonmultipart import MIMENonMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
#Sends email if the item is still out of stock

#Enter Credentials here for the gmail account you will send notifications from.
#note that the password should be the gmail api password and not the actual password to log in.
gUser = ""
gPass = ""
#recipient email address goes here.
recipient =""

#Carrier information to send SMS via email if you would ilke
#Noted Spint and Tmobile here to cover my cases
#[insert 10-digit number]@messaging.sprintpcs.com
#[insert 10-digit number]@tmomail.net


def sendNotif(email):
    try:
        #create new SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        
        #Add TLS
        server.starttls()

        #Authenticate into Gmail account using the email and gmail API password store above.
        server.login(gUser,gPass)

        #Don't need to define message, because we will use email string sent to method
        #Build Message:

        msg = MIMEMultipart()
        msg['From'] = gUser
        msg['To'] = recipient
        msg['Subject'] = 'Micro Center Out Of Stock Notification'
        msg.attach(MIMEText(email,'plain'))
        text = msg.as_string()

        #Send email:
        server.sendmail(gUser,recipient,text)

        #Close session:
        server.quit()
        print("Email sent Successfully!")

    except Exception as ex:
        print("Something Went Wrong ",ex)
    