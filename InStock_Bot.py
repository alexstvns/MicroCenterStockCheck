#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as OP
from selenium.webdriver.support import expected_conditions as EC
import SMS
import emailNotif
import time

# Please note that you will need to do the following before this will work
# 1. Install the geckodriver and Firefox browser to allow you to run Firefox using the selenium webdriver.
# 2. edit and configure the SMS.py and emailNotif.py scripts to enter your email and API information
# NOTE: this may require you to have a spare gmail account and/or Twilio account to use.
# 3. You will need to install the selenium and twilio packages through python PIP to use the webdriver and SMS functions
# NOTE: you do not need to install twilio if you choose to only use email notifications.
# 
#  




# NOTE: the commented out code below will allow you to run the script in headless mode which wont require a GUI. (good for running on a server.)
# you can uncomment this out but you will need to comment out the sDriver = webdriver.Firefox() below. 
#options = OP()
#options.headless = True
#sDriver = webdriver.Firefox(options=options)
sDriver = webdriver.Firefox()

#Link for tustin microcenter item page should go here:
linkTar = "https://www.microcenter.com/product/641411/lenovo-legion-5-173-gaming-laptop-computer-blue"


sDriver.get(linkTar)



itemName =sDriver.find_element(By.CSS_SELECTOR,'#product-details-control #details h1').text

try:
    #see if the store selector is present, if it is choose the first item which is the ca- Tustin store.
    # and click that selection.
    elem = WebDriverWait(sDriver, 5).until(
        EC.presence_of_element_located((By.ID,'storeInfo'))
        
    )
    tustin = sDriver.find_element(By.CLASS_NAME,'dropdown-item').click()

finally:  
    el = sDriver.find_element(By.CLASS_NAME,'inventory')
    searchString = el.text

    if(searchString.find('SOLD OUT') != -1):
        print('Still Out of Stock')
        #triggers an email notificationto get sent you can also comment this out and send a text message by
        # using the SMS.sendText(itemName+' Is Still Out Of Stock) function.
        emailNotif.sendNotif(itemName+' Is Still Out Of Stock', 'MicroCenter Out Of Stock Notification')
    else:

        #If the item is in stock send a text and email to the recipient number/emails listed in emailNotif and SMS.py also inlcude the target link so the user 
        #quickly access. 
        numStock = sDriver.find_element(By.CLASS_NAME,'inventoryCnt').text
        bodyMessage = 'Your Item: '+ itemName + '\nHas: ' +numStock + '\n \n' + linkTar
        print(bodyMessage)

        # Send text message if available include inventory count.
        SMS.sendText(bodyMessage)
        # Note; you can comment out the SMS.sendText(bodyMessage) and replace it with
        emailNotif.sendNotif(bodyMessage,'MicroCenter In Stock Notification') 
        #this will cause an email to be sent to the user instead of an SMS.

    time.sleep(2)
    sDriver.close()
exit()
