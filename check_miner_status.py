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
import datetime

def restartMiner():
   os.system("taskkill /f /im  miner.exe")
   sleep(5)
   os.chdir("C:/Users/Syunik1/Desktop/0.3.4b")
   os.startfile("fypool.bat")
   sleep(60)

def send_email(reason):
   try:
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()

      #Next, log in to the server
      server.login("soltiteam", "")

      #Send the mail
      sent_from = 'soltiteam@gmail.com'
      to = ['mkrtchyan.mushegh@gmail.com', 'tigranmur@gmail.com']
      message = 'Subject: {}\n\n{}'.format('Restart!', 'snk1 was restarted, reason: {}'.format(reason))
      server.sendmail(sent_from, to, message)
      server.quit()
   except:
      print("ERROR: Can't send an email")   


print('will start miner check within 60 sec...')
sleep(60)
errorCounter = 0
os.environ['NO_PROXY'] = '127.0.0.1'
while True:
  hashrates = []
  temps = []
  powers = []
  shares = []
  try:
    r = requests.get('http://127.0.0.1:42000/getstat')
    json = r.json()
    error = json['error']
    results = json['result']
    numberOfGPUs = len(results)
    print('number of GPUs: {}'.format(numberOfGPUs))
    for i in range(numberOfGPUs):
      currentGPUhashrate = results[i]['speed_sps']
      currentGPUtemp = results[i]['temperature']
      currentGPUpower = results[i]['gpu_power_usage']
      currentAcceptedShares = results[i]['accepted_shares']
      hashrates.append(currentGPUhashrate)
      temps.append(currentGPUtemp)
      powers.append(currentGPUpower)
      shares.append(currentAcceptedShares)
      print('GPU{}: {}, accepted shares: {}'.format(i, currentGPUhashrate, currentAcceptedShares))
    #print('error: {}'.format(error))

    print('Total hashrate: {}, total shares: {}'.format(sum(hashrates), sum(shares)))

    try:
       r2 = requests.post("http://artkaren.com/", 
            data={'miner': 'Syunik1',
                 'gpu0': hashrates[0], 'gpu0temp': temps[0], 'gpu0power': powers[0],
                 'gpu1': hashrates[1], 'gpu1temp': temps[1], 'gpu1power': powers[1],
                 'gpu2': hashrates[2], 'gpu2temp': temps[2], 'gpu2power': powers[2],
                 'gpu3': hashrates[3], 'gpu3temp': temps[3], 'gpu3power': powers[3],
                 'gpu4': hashrates[4], 'gpu4temp': temps[4], 'gpu4power': powers[4],
                 'gpu5': hashrates[5], 'gpu5temp': temps[5], 'gpu5power': powers[5],
                 'pytime': datetime.datetime.utcnow()})
       print(r2.status_code, r2.reason)
       #print(r2.text)
    except:
       print('Error sending data to the server')
    
    hashrates.sort()
    if hashrates[0] < 100:
      print("one of the GPU's hashrate is less than 100 Sol/s, restart...")
      send_email("one of the GPU's hashrate is less than 100 Sol/s")
      restartMiner()
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
      errorCounter = 0
      restartMiner()

