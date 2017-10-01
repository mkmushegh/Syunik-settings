#!/usr/bin/env python

#t1RJ3hvzPQsVHe89yjiTo9XbyfFMbCz8EKa - zcash

from urllib.request import urlopen, Request #Needed to make the requests to the nanopool api 
import json #Needed to create json objects with the data from the api                                         
import os                  
from time import sleep 
import smtplib

def get_hashrate(url):
   count = 0 #Sets the count variable to 0
   while True: #Repeats the procedure until hashrate is returned
      try:
         req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #Requests the url like Mozilla 5.0 to avoid http error 403           
         info = json.loads(urlopen(req).read().decode('utf-8')) #Creates the json object "info" with the data from the api          
         if info['status']: #If didn't occur errors                         
            return int(info['data']['currentHashrate']) #Returns the hashrate                      
         else: #If did occur an error                                                  
            print('Nanopool API: '+ info['error'] + ', trying again in 30 seconds')   #Logs the error  
         sleep(30)
      except:
         print("Can't connect to the pool, maybe interner connection issue. Will try again in 15 sec..." )
         sleep(15)

def check_hashrate(url):
   """
   insert anything you like here
   it can be on multiple lines. describe 
   the whole function.
   """
   count = 0 #Sets the count variable to 0
   while True: #Makes a infinite loop for this function to run all the time
      sleep(15)
      hash = get_hashrate(url)
      if hash < 2000: #If the hashrate is 0            
         count += 1 #Adds 1 to the count variable             
         print('Hashrate seems to be less than 2000') #Logs a warning
      
      else: #If the hashrate is greater then 2000                                    
         print('Hashrate: {}'.format(hash))
         count = 0 #Sets the count variable to 0
         
      if count == 2: #If the count variable is 2 (you can change it to 1 if you want to risk false positives)          
         print('Restarting the system within 15 sec...')
         send_email()
         sleep(15)
         os.system('reboot')    

def send_email():
   try:
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()

      #Next, log in to the server
      server.login("soltiteam", "Syunik1234")

      #Send the mail
      sent_from = 'soltiteam@gmail.com'
      to = ['mkrtchyan.mushegh@gmail.com', 'tigranmur@gmail.com']
      message = 'Subject: {}\n\n{}'.format('Restart!', 'snk2 was restarted')
      server.sendmail(sent_from, to, message)
      server.quit()
      print("Kuklinery texekacvac en")
   except:
      print("Something went wronge")    

print('Will start the pool check within 20 min...')
sleep(1200)
print('Start checking')
print(check_hashrate('https://api-zcash.flypool.org/miner/:t1RJ3hvzPQsVHe89yjiTo9XbyfFMbCz8EKa/worker/:syunik2_ubuntu/currentStats'))


