
import requests
import sys
import os
import time
import logging
import smtplib

from email.message import Email.Message

def check_status_node1():
 s = os.popen("/bin/curl -kv https://x293823:8443 2>&1 | grep -w '* Failed' | awk '{print $6 $7}' ")
 
 node1_status = s.read()
 
 if node1_status:
  time.sleep(30)
  s = os.popen("/bin/curl -kv https://jenkins.com:8443 2>&1 | grep -w '* Failed' | awk '{print $6 $7}' ")
  
  jenkins_url_status = os.popen("/bin/curl -kv https://jenkins.com:8443 2>&1 | grep -w 'Network file descriptor is not connected'")
  
  if jenkins_url_status:
   s.close()
   return True
   
 s.close()
 return False
 
 def send_email():
  textfile = '/users/jenkins/Monitoring/jenkins-ha-failover/emailcontext.txt'
  
  
  
# Open the plain text file whose name is in textfile for reading.

  with open(textfile) as fp:
   msg = EmailMessage()
   msg.set_content(fp.read())
  
 
  msg['Subject'] = 'Jenkins1 Failover'
  msg['From'] = "x945287"
  msg['To'] = "Dev@sas.com"
  
 # Send the message via our own SMTP server
 
  s = smtplib.SMTP('localhost')
  s.send_message(msg)
  s.quit()
  
  
  
 def write_log(status):
  log_file = '/users/jenkins/Monitoring/jenkins-ha-failover/logs/failover.log'
  logging.basicConfig(filename=log_file, format= '%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, filemode='a')
  logger = logging.getLogger()
  if status=="node1":
   logger.info("Running on node1 - x232323")
  else:
   logger.info("Running on node2 - x443423")
  
  
  
 def main():
 
 status = check_status_node1()
 s = os.popen("/bin/curl -kv https://x293823:8443 2>&1 | grep -w '* Failed' | awk '{print $6 $7}' ")
 node2_status = s.read()
 
 
 if status and node2_status():
  os.system('systemctl start jenkins.service')
  time.sleep(20)
  write_log("node2")
  send_email()
  os.close()
 
 else: write_log("node1")
  
 if _name_ == " _main_ ":
   main()
