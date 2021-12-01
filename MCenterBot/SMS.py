from twilio.rest import Client
import emailNotif

#Twilio account SID and Account Auth Token Go here:
account_sid = ""
account_token = ""






def sendText(bodyMessage):
    try:
        #Initiate Twilio and pass SID / Token
        tClient = Client(account_sid, account_token)
        #Build SMS text message and send t recipient number. 
        tClient.messages.create(
        # enter the SMS number you would like to send a msg to.
        to = "+", 
        #Enter your Twilio SMS phone number here.
        from_ = "+", 
        body = bodyMessage)
        print('Text Sent')
    except Exception as ex:
        print('SMS Message Failed ', ex)
        emailNotif.sendNotif('SMS Failed ',ex)