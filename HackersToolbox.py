#Made by J0K3RS-L4UGH

import os

#already availiable tools:

#WhoIs
#sqlmap
#netcat
#nmap
#hashcat
#crunch
#cupp
#sherlock

#tools to add

#aircrack-ng
#wifite

#types of tools to add

#wifi hacking
#wirless hacking

#Classing the colored text
class bcolors:
	IDK = '\033[31m'
	ENDC = '\033[0m'
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


#starting the home page
os.system('clear')

print(f'''{bcolors.IDK}
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███    ██████      
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒      
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒░ ▓██▄        
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒     
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒▒██████▒▒     
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░     
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░     
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ ░  ░  ░       
 ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░           ░       
                  ░                                             
   ▄▄▄█████▓ ▒█████   ▒█████   ██▓     ▄▄▄▄    ▒█████  ▒██   ██▒
   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░
   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▒██▒ ▄██▒██░  ██▒░░  █   ░
   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▒██░█▀  ▒██   ██░ ░ █ █ ▒ 
     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒
     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░
     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░    ░    ░ ░ ░ ░ ▒   ░    ░  
                ░ ░      ░ ░      ░  ░ ░          ░ ░   ░    ░  
                                            ░                   
                                    {bcolors.ENDC}''')


#Info Gathering
print(f'{bcolors.OKGREEN}[1] Information Gathering:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Nmap\n\tWhoIs\n\tSherlock{bcolors.ENDC}')

#Password Attacks
print(f'{bcolors.OKGREEN}[2] Password Attacks{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Crunch\n\tHashCat\n\tCupp{bcolors.ENDC}')

#Networking
print(f'{bcolors.OKGREEN}[3] Networking{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Nmap\n\tNetCat{bcolors.ENDC}')

#Web Hacking
print(f'{bcolors.OKGREEN}[4] Web Hacking:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}SQLMap{bcolors.ENDC}')

#About
print(f'{bcolors.OKGREEN}[5] About{bcolors.ENDC}')

#Exit
print(f'{bcolors.OKGREEN}[6] Exit{bcolors.ENDC}')

#asking what type of tool they want to use
first = input('What type of tool would you like to use?:\n')

#if the answer is 1, start the info gathering menu
if first == '1':
	os.system('clear')
	print(f'{bcolors.OKGREEN}Information Gathering:{bcolors.ENDC}')
	print(f'\t{bcolors.OKCYAN}[1] Nmap')
	print(f'\t[2] WhoIs')
	print(f'\t[3] Sherlock{bcolors.ENDC}')
	idk1 = input('What tool would you like to use?:\n')

    #if nmap is selected
	if idk1 == '1':
		os.system('clear')
		os.system('nmap -h')
		ncommand1 = input('What Nmap command would you like to run? (Usage: nmap [Scan Type(s)] [Options] {target specification}):\n')
		os.system('clear')
		os.system(ncommand1)

    #if whois is selected
	if idk1 == '2':
		os.system('clear')
		os.system('whois -h')
		whoisl = input('What WhoIs command do you want to run? (Usage: whois [OPTION]... OBJECT...):\n')
		os.system('clear')
		os.system(whoisl)

    #if sherlock is selected
	if idk1 == '3':
		username1 = input('What username would you like to search?:\n')
		os.system('clear')
		os.system('python3 .sherlock/sherlock/sherlock/sherlock.py' + ' ' + username1)

#if answer is 2, start the password hacking menu
if first == '2':
	os.system('clear')
	print(f'{bcolors.OKGREEN}Password Attacks:{bcolors.ENDC}')
	print(f'\t{bcolors.OKCYAN}[1] Crunch')
	print(f'\t[2] HashCat\n\t[3] Cupp\n\t[4] John the Ripper\n\t[5] Hydra{bcolors.ENDC}')
	idk2 = input('What tool would you like to use?:\n')

	if idk2 == '1':

        #if crunch is selected
		os.system('clear')
		crunchmin = input('What is the minimum amount of characters you would like to include in 1 password?: ')
		crunchmax = input('What is the maximum amount of characters you would like to include in 1 password?: ')
		crunchchar = input('What characters would you like to have in the wordlist? (i.e. abc123)?: ')
		crunchname = input('What file would you like the wordlist to be stored in? (Please include the file extention)(i.e. wordlist.txt): ')
		os.system('clear')
		os.system('crunch ' + crunchmin + ' ' + crunchmax + ' ' + crunchchar + ' -o ' + crunchname)

    #if hashcat is selected
	if idk2 == '2':
		os.system('clear')
		hashstuff = input('What HashCat command would you like to run? (Usage: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...):\n')
		os.system('clear')
		os.system(hashstuff)

    #if cupp is selected
	if idk2 == '3':
                os.system('clear')
                os.system('cupp -i')

	if idk2 == '4':
                os.system('clear')
		os.system('john')
                johnstuff = input('What John the Ripper command would you like to run? (Usage: john [OPTIONS] [PASSWORD-FILES]):\n')
                os.system('clear')
                os.system(johnstuff)

	if idk2 == '4':
                os.system('clear')
                os.system('hydra -h')
                hydrastuff = input('What Hydra command would you like to run? (Usage: Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]):\n')
                os.system('clear')
                os.system(hydrastuff)

#if answer is 3, start the network hacking menu
if first == '3':
	os.system('clear')
	print(f'{bcolors.OKGREEN}Networking:{bcolors.ENDC}')
	print(f'\t{bcolors.OKCYAN}[1] Nmap')
	print(f'\t[2] NetCat{bcolors.ENDC}')
	idk3 = input('What tool would you like to use?:\n')

    #if nmap is selected
	if idk3 == '1':
                os.system('clear')
                os.system('nmap -h')
                ncommand2 = input('What Nmap command would you like to run? (Usage: nmap [Scan Type(s)] [Options] {target specification}):\n')
                os.system('clear')
                os.system(ncommand2)

    #if netcat is selected
	if idk3 == '2':
                os.system('clear')
                os.system('netcat -h')
                ncommand3 = input('What NetCat command do you want to run? usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl] [-m minttl] [-O length] [-P proxy_username] [-p source_port] [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout] [-X proxy_protocol] [-x proxy_address[:port] [destination] [port]')
                os.system('clear')
                os.system(ncommand3)

#if answer is 4, start the web hacking menu
if first == '4':
	os.system('clear')
	print(f'{bcolors.OKGREEN}Web Hacking:{bcolors.ENDC}')
	print(f'\t{bcolors.OKCYAN}[1] SQLMap')
	idk4 = input('What tool would you like to use?:\n')

    #if SQLMap is selected
	if idk4 == '1':
		os.system('clear')
		os.system('sqlmap -h')
		squestion = input('What SQLMap command do you want to run? (Usage: sqlmap [website]):')
		os.system(squestion)


if first == '5':
	os.system('clear')
	print(f'{bcolors.OKGREEN}About:{bcolors.ENDC}')
	print(f'This collection of tools was made by J0K3RS-L4UGH\nLinks:\n{bcolors.UNDERLINE}https://github.com/J0K3RS-L4UGH\nhttps://j0k3rs-l4ugh.github.io/{bcolors.ENDC}')
	print('Bye')


if first == '6':
	os.system('clear')
	print('Bye')
