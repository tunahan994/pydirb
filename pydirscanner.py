#Author: Ast3rpiX
#Github: https://github.com/tunahan994

import requests
from colorama import Fore
import sys
import os
import argparse

def banner():
	print(f"""{Fore.BLUE}
 ____            _ _                                          
|  _ \ _   _  __| (_)_ __ ___  ___ __ _ _ __  _ __   ___ _ __ 
| |_) | | | |/ _` | | '__/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
|  __/| |_| | (_| | | |  \__ \ (_| (_| | | | | | | |  __/ |   
|_|    \__, |\__,_|_|_|  |___/\___\__,_|_| |_|_| |_|\___|_|   
       |___/                                                  
            {Fore.RESET}""")




def dir_scan(url,wordlist,save,filename):
	array = []

	try:
		
		if url[:7] != "http://":
			url = "http://" + url

		site = requests.get(url)
		
		if site.status_code == 200:
			print(f'{Fore.GREEN}Host is up.{Fore.RESET}')
		
		else:
			print(f'{Fore.RED}Host is down.{Fore.RESET}')
			sys.exit(1)
		
		if os.path.exists(wordlist):
			file = open(wordlist,"r")
			
			print(f"{Fore.BLUE}URL: {url}\n{Fore.RESET}")
			print(f"{Fore.GREEN}Attack is starting...\n{Fore.RESET}")

			for i in file:
				
				req = requests.get(url + "/" + i)
				
				if req.status_code == 200:
					print("".rjust(len(url+ "/" + i)+ 5,'-'))
					print(f"{Fore.GREEN}")
					print(str("Directory Found: " + url + "/" + i))
					print(f"{Fore.RESET}")	
					array.append(str(i))			
				else:
					pass
			
			file.close()

			if save.lower().strip() == "accept":
				save = open(filename,"a",encoding="utf-8")
				save.write("Directory scan results for {}\n".format(url))
				save.write("--------------------------------------------\n")
				for i in array:
					save.write("/{}\n".format(i))
				save.close()			
				
		else:
			print(wordlist + " don't exists in the directory.")
	
	except Exception as e:
		print(e)

if os.name == "posix":
	os.system("clear")
	banner()
	parser = argparse.ArgumentParser(description="Python Dirbuster")
	parser.add_argument(
		"--wordlist",
		type = str,
		metavar = "<Location>",
		help = "Wordlist Location --For example-> /usr/share/wordlists/rockyou.txt",
		default = "/usr/share/wordlists/dirb/common.txt"
	)
	parser.add_argument(
		"--target",
		type = str,
		metavar = "<URL>",
		help = "URL with http:// (Don't use https) ",

	)
	parser.add_argument(
		"--save",
		type = str,
		metavar = "<accept/refuse>",
		help = "Save scan result",
		default = "accept"
	)
	parser.add_argument(
		"--filename",
		type = str,
		metavar = "<Out file name>",
		help = "Output files",
		default = "output.txt"
	)

	args = parser.parse_args()
	wordlist = args.wordlist
	target = args.target
	save = args.save
	filename = args.filename

	if not target:
		parser.print_help()
		sys.exit(1)

	dir_scan(target,wordlist,save,filename)	
else:
	print(f"{Fore.RED}Your machine is {os.name} please use a posix opearting system{Fore.RESET}")

