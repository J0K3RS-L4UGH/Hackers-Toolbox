#!/bin/bash

yes="y"

CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "Terms of sevice:\n1. The creator of this tool can not be held liable for any of your actions involving this script\n2. No illegal actions will be commited with this script\nDo you accept these Terms and Conditions? [y/n]:"
read tnc

if [ $tnc = $yes ]
then
  sudo apt-get update -y && sudo apt-get upgrade -y


  echo -e "\n${CYAN}[+]${GREEN} Installing WhoIs${NC}\n"
  sudo apt-get install whois -y

  echo -e "\n${CYAN}[+]${GREEN} Installing SQLMap${NC}\n"
  sudo apt-get install sqlmap -y

  echo -e "\n${CYAN}[+]${GREEN} Installing NetCat${NC}\n"
  sudo apt-get install netcat -y

  echo -e "\n${CYAN}[+]${GREEN} Installing NMap${NC}\n"
  sudo apt-get install nmap -y

  echo -e "\n${CYAN}[+]${GREEN} Installing HashCat${NC}\n"
  sudo apt-get install hashcat -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Crunch${NC}\n"
  sudo apt-get install crunch -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Cupp${NC}\n"
  sudo apt-get install cupp -y

  echo -e "\n${CYAN}[+]${GREEN} Installing John the Ripper${NC}\n"
  sudo apt-get install john -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Hydra${NC}\n"
  sudo apt-get install hydra -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Wifite${NC}\n"
  sudo apt-get install wifite -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Go${NC}\n"
  sudo apt-get install golang -y

  echo -e "\n${CYAN}[+]${GREEN} Installing TShark${NC}\n"
  sudo apt-get install tshark -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Steghide${NC}\n"
  sudo apt-get install steghide -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Bully${NC}\n"
  sudo apt-get install bully -y

  echo -e "\n${CYAN}[+]${GREEN} Installing Hakrawler${NC}\n"
  go get github.com/hakluke/hakrawler

  echo -e "\n${CYAN}[+]${GREEN} Installing Sherlock${NC}\n"
  sudo mkdir .sherlock
  cd .sherlock
  sudo git clone https://github.com/sherlock-project/sherlock.git
  cd sherlock
  sudo pip3 install -r requirements.txt

  cd ..
  cd ..

  echo -e "\n${CYAN}[+]${GREEN} Installing PayDuck${NC}\n"

  sudo mkdir .payduck
  cd .payduck
  sudo git clone https://github.com/J0K3RS-L4UGH/PayDuck/

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
  echo 'DELETED MAIN FILE'
fi
