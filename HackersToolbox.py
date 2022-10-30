# Made by J0K3RS-L4UGH

import os
import time

# already availiable tools:

# WhoIs
# sqlmap
# netcat
# nmap
# hashcat
# crunch
# cupp
# sherlock

# tools to add

# aircrack-ng

# types of tools to add

# Classing the colored text


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


# starting the home page
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


# Info Gathering
print(f'{bcolors.OKGREEN}[1] Information Gathering:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Nmap\n\tWhoIs\n\tSherlock{bcolors.ENDC}')

# Password Attacks
print(f'{bcolors.OKGREEN}[2] Password Attacks{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}HashCat\n\tJohn the Ripper\n\tHydra{bcolors.ENDC}')

# Networking
print(f'{bcolors.OKGREEN}[3] Networking{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Nmap\n\tNetCat\n\tTShark{bcolors.ENDC}')

# Web Hacking
print(f'{bcolors.OKGREEN}[4] Web Hacking:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}SQLMap\n\tHakrawler{bcolors.ENDC}')

# WiFi Hacking
print(f'{bcolors.OKGREEN}[5] WiFi Hacking:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Wifite{bcolors.ENDC}')

# wordlist gens
print(f'{bcolors.OKGREEN}[6] Wordlist Generators:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Crunch\n\tCupp{bcolors.ENDC}')

# wordlist gens
print(f'{bcolors.OKGREEN}[7] Image Hacking:{bcolors.ENDC}')
print(f'\t{bcolors.OKCYAN}Steghide{bcolors.ENDC}')

# About
print(f'{bcolors.OKGREEN}[8] About{bcolors.ENDC}')

# Exit
print(f'{bcolors.OKGREEN}[9] Exit{bcolors.ENDC}')

# asking what type of tool they want to use
tooltype = input('What type of tool would you like to use?:\n')

# if the answer is 1, start the info gathering menu
if tooltype == '1':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Information Gathering:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] Nmap')
    print(f'\t[2] WhoIs')
    print(f'\t[3] Sherlock{bcolors.ENDC}')
    infogath = input('What tool would you like to use?:\n')

# if nmap is selected
    if infogath == '1':
        os.system('clear')
        os.system('nmap -h')
        ncommand1 = input(
            'What Nmap command would you like to run? (Usage: nmap [Scan Type(s)] [Options] {target specification}):\n')
        os.system('clear')
        os.system('sudo' + ' ' + ncommand1)

# if whois is selected
    if infogath == '2':
        os.system('clear')
        os.system('whois -h')
        whoisl = input(
            'What WhoIs command do you want to run? (Usage: whois [OPTION]... OBJECT...):\n')
        os.system('clear')
        os.system('sudo' + ' ' + whoisl)

# if sherlock is selected
    if infogath == '3':
        username1 = input('What username would you like to search?:\n')
        os.system('clear')
        os.system(
            'python3 ~/Hackers-Toolbox/.sherlock/sherlock/sherlock/sherlock.py' + ' ' + username1)

# if answer is 2, start the password hacking menu
if tooltype == '2':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Password Attacks:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] HashCat\n\t[2] John the Ripper\n\t[3] Hydra{bcolors.ENDC}')
    attkpasswd = input('What tool would you like to use?:\n')

# if hashcat is selected
    if attkpasswd == '1':
        os.system('clear')
        hashstuff = input(
            'What HashCat command would you like to run? (Usage: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...):\n')
        os.system('clear')
        os.system('sudo' + ' ' + hashstuff)

    if attkpasswd == '2':
        os.system('clear')
        os.system('john')
        johnstuff = input(
            'What John the Ripper command would you like to run? (Usage: john [OPTIONS] [PASSWORD-FILES]):\n')
        os.system('clear')
        os.system('sudo' + ' ' + johnstuff)

    if attkpasswd == '3':
        os.system('clear')
        os.system('hydra -h')
        hydrastuff = input(
            'What Hydra command would you like to run? (Usage: Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]):\n')
        os.system('clear')
        os.system('sudo' + ' ' + hydrastuff)

# if answer is 3, start the network hacking menu
if tooltype == '3':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Networking:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] Nmap')
    print(f'\t[2] NetCat\n\t[3] TShark{bcolors.ENDC}')
    netwkhak = input('What tool would you like to use?:\n')

# if nmap is selected
    if netwkhak == '1':
        os.system('clear')
        os.system('nmap -h')
        ncommand2 = input(
            'What Nmap command would you like to run? (Usage: nmap [Scan Type(s)] [Options] {target specification}):\n')
        os.system('clear')
        os.system('sudo' + ' ' + ncommand2)

    # if netcat is selected
    if netwkhak == '2':
        os.system('clear')
        os.system('netcat -h')
        ncommand3 = input(
            'What NetCat command do you want to run? usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl] [-m minttl] [-O length] [-P proxy_username] [-p source_port] [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout] [-X proxy_protocol] [-x proxy_address[:port] [destination] [port]:\n')
        os.system('clear')
        os.system('sudo' + ' ' + ncommand3)
    
    if netwkhak == '3':
        os.system('clear')
        os.system('tshark -h')
        ts = input(
            'What TShark command do you want to run? usage : tshark [options]:\n')
        os.system('clear')
        os.system('sudo' + ' ' + ts)

# if answer is 4, start the web hacking menu
if tooltype == '4':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Web Hacking:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] SQLMap\n\t[2] Hakrawler{bcolors.ENDC}')
    webhak = input('What tool would you like to use?:\n')

# if SQLMap is selected
    if webhak == '1':
        os.system('clear')
        os.system('sqlmap -h')
        squestion = input('What SQLMap command do you want to run? (Usage: sqlmap [website]):\n')
        os.system('sudo' + ' ' + squestion)

# if hakrawler is selected
    if webhak == '2':
        os.system('clear')
        krawlurl = input('What URL do you want to crawl (i.e. https://www.example.com/):\n')
        os.system('echo ' + krawlurl + ' | ~/go/bin/hakrawler')    
    

# if answer is 5, start the wifi hacking menu
if tooltype == '5':
    os.system('clear')
    print(f'{bcolors.OKGREEN}WiFi Hacking:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] Wifite')
    wifihak = input('What tool would you like to use?:\n')

# if Wifite is selected
    if wifihak == '1':
        os.system('clear')
        # os.system('wifite -h')
        wifitequestion = input('What is the path to the wordlist you want to use? (/path/to/your/wordlist.txt):\n')
        print('The command is:\nsudo wifite --dict ' + wifitequestion + ' --kill')
        time.sleep(2)
        os.system('sudo wifite --dict ' + wifitequestion + ' --kill')
        
# if answer is 6, start the wordlist generator menu
if tooltype == '6':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Wordlist Generators:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] Crunch\n\t[2] Cupp{bcolors.ENDC}')
    idk6 = input('What tool would you like to use?:\n')

    if idk6 == '1':

        # if crunch is selected
        os.system('clear')
        crunchmin = input(
            'What is the minimum amount of characters you would like to include in 1 password?: ')
        crunchmax = input(
            'What is the maximum amount of characters you would like to include in 1 password?: ')
        crunchchar = input(
            'What characters would you like to have in the wordlist? (i.e. abc123)?: ')
        crunchname = input(
            'What file would you like the wordlist to be stored in? (Please include the file extention)(i.e. wordlist.txt): ')
        os.system('clear')
        os.system('sudo' + ' ' + 'crunch ' + crunchmin + ' ' + crunchmax + ' ' + crunchchar + ' -o ' + crunchname)      
        
    if idk6 == '2':
        os.system('clear')
        os.system('sudo' + ' ' + 'cupp -i')
        
if tooltype == '7':
    os.system('clear')
    print(f'{bcolors.OKGREEN}Image Hacking:{bcolors.ENDC}')
    print(f'\t{bcolors.OKCYAN}[1] Steghide{bcolors.ENDC}')
    idk6 = input('What tool would you like to use?:\n')

    if idk6 == '1':
        print('To embed emb.txt in cvr.jpg: steghide embed -cf cvr.jpg -ef emb.txt\nTo extract embedded data from stg.jpg: steghide extract -sf stg.jpg')
        whtimg = input('What steghide command do you want to run?:\n')
        os.system('sudo ' + whtimg)
        
if tooltype == '8':
    os.system('clear')
    print(f'{bcolors.OKGREEN}About:{bcolors.ENDC}')
    print(f'This collection of tools was made by J0K3RS-L4UGH\nLinks:\n{bcolors.UNDERLINE}https://github.com/J0K3RS-L4UGH\nhttps://j0k3rs-l4ugh.github.io/{bcolors.ENDC}')
    print('Bye')


if tooltype == '9':
    os.system('clear')
    print('Bye')
