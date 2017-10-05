#!/usr/bin/env python

'''
THIS SCRIPT IS WRITTEN BY M.MKRTCHYAN, 2017
IF YOU FIND IT USEFUL YOU CAN MAKE A DONATION
ZCASH - t1RJ3hvzPQsVHe89yjiTo9XbyfFMbCz8EKa
'''

import requests
from time import sleep 
import smtplib
import os

def send_email(reason):
   try:
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()

      #Next, log in to the server
      server.login("soltiteam", "Syunik1234")

      #Send the mail
      sent_from = 'soltiteam@gmail.com'
      to = ['mkrtchyan.mushegh@gmail.com', 'tigranmur@gmail.com']
      message = 'Subject: {}\n\n{}'.format('Restart!', 'snk3 was restarted, reason: {}'.format(reason))
      server.sendmail(sent_from, to, message)
      server.quit()
   except:
      print("ERROR: Can't send an email")   


print('will start miner check within 60 sec...')
sleep(60)
errorCounter = 0
while True:
  hashrates = []
  try:
    r = requests.get('http://127.0.0.1:42000/getstat')
    json = r.json()
    error = json['error']
    results = json['result']
    numberOfGPUs = len(results)
    print('number of GPUs: {}'.format(numberOfGPUs))
    for i in range(numberOfGPUs):
      currentGPUhashrate = results[i]['speed_sps']
      hashrates.append(currentGPUhashrate)
      print('GPU{}: {}'.format(i, currentGPUhashrate))
    #print('error: {}'.format(error))

    hashrates.sort()
    if hashrates[0] < 350:
      print("one of the GPU's hashrate is less than 350 Sol/s, restart...")
      send_email("one of the GPU's hashrate is less than 350 Sol/s")
      os.system('reboot') 
    sleep(30)
  except:
    if errorCounter < 5:
      print('error connecting to http://127.0.0.1:42000, will try again in 10 sec...')
      errorCounter += 1
      sleep(10)
    else:
      print('too many errors, restarting the system in 10 sec...')
      send_email("error connecting to http://127.0.0.1:42000 to many times")
      sleep(10)
      os.system('reboot') 

