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

sudo mkdir .sherlock
cd .sherlock
sudo git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
sudo pip3 install -r requirements.txt

cd ..

y="y"
n="n"
echo "Would you like to run Hackers Toolbox (python3 HackersToolbox.py)? [y/n]:"
read yn
if [ $yn == $y ]
then
 python3 HackersToolbox.py
else
  echo 'Thanks for installing!'
fi
