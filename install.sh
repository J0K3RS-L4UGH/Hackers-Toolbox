echo 'What directory would you like Hackers Toolbox to be installed in? (for /bin press enter)' 
read dir
bin=""

if [ $dir == $bin]
then
  cd /bin
else
  cd $dir
fi

sudo git clone https://github.com/J0K3RS-L4UGH/Hackers-Toolbox.git


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

cd
echo 'What is your shells config file? '


rm -r install.sh
