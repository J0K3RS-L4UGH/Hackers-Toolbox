sudo apt-get update && sudo apt-get upgrade

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

mkdir .sherlock
cd .sherlock
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip3 install -r requirements.txt
pip freeze > requirements.txt
cd ..
cd ..
