#!/bin/bash

yes="y"

echo -e "Terms of sevice:\n1. The creator of this tool can not be held liable for any of your actions involving this script\n2. No illegal actions will be commited with this script\nDo you accept these Terms and Conditions? [y/n]:"
read tnc

if [ $tnc = $yes ]
then
  sudo apt-get update -y && sudo apt-get upgrade -y

  sudo apt-get install whois -y

  sudo apt-get install sqlmap -y

  sudo apt-get install netcat -y

  sudo apt-get install nmap -y

  sudo apt-get install hashcat -y

  sudo apt-get install crunch -y

  sudo apt-get install cupp -y

  sudo apt-get install john -y

  sudo apt-get install hydra -y

  sudo apt-get install wifite -y
  
  sudo apt-get install golang -y
  
  sudo apt-get install tshark -y

  go get github.com/hakluke/hakrawler@latest

  sudo mkdir .sherlock
  cd .sherlock
  sudo git clone https://github.com/sherlock-project/sherlock.git
  cd sherlock
  sudo pip3 install -r requirements.txt

  cd ..
  cd ..
  
  y="y"
  n="n"
  echo "Would you like to run Hackers Toolbox (python3 HackersToolbox.py)? [y/n]:"
  read yn
  if [ $yn = $y ]
  then
   python3 HackersToolbox.py
  else
    echo 'Thanks for installing!'
  fi
else
  sudo rm -r HackersToolbox.py
  echo 'Sorry'
fi
