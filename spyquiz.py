#!/usr/bin/env python
#coding: utf-8

'''
SPY
'''

from time import *
import hashlib
import getpass
import sys
import os
from platform import python_version

Limpar = "clear"

os.system(Limpar)

if sys.version_info[0] < 3:
	versao = python_version()
	print("\n\033[32m  You are using python in version\033[1;m \033[1m\033[31m%s\033[1;m \033[32me and it is lower than python3 onwards.\033[1;m" %(versao))
	print("\033[32m Please run the Spy-Quiz with the higher version than python2.\033[1;m\n")
	exit(1)
print("""\033[41m
☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ 
☰       ╦  ╦╔═╗╔╦╗╔═╗╔═╗  ╦  ╔═╗ ┬        ☰ 
☰       ╚╗╔╝╠═╣║║║║ ║╚═╗  ║  ╠═╣ │        ☰ 
☰        ╚╝ ╩ ╩╩ ╩╚═╝╚═╝  ╩═╝╩ ╩ o        ☰ 
☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ \033[1;m
""")
try:
	print("\n\033[31mEnter a user name for this session:\033[1;m \n")
	usuario = input("\033[1;32m▬▶\033[1;m  ").upper()
except:
	exit(1)

def Apresentacao():
	os.system(Limpar)
	print("""\033[35m

  ██████  ██▓███ ▓██   ██▓     █████   █    ██  ██▓▒███████▒
▒██    ▒ ▓██░  ██▒▒██  ██▒   ▒██▓  ██▒ ██  ▓██▒▓██▒▒ ▒ ▒ ▄▀░
░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   ▒██▒  ██░▓██  ▒██░▒██▒░ ▒ ▄▀▒░
  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   ░██  █▀ ░▓▓█  ░██░░██░  ▄▀▒   ░
▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   ░▒███▒█▄ ▒▒█████▓ ░██░▒███████▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▓  ░▒▒ ▓░▒░▒
░ ░▒  ░ ░░▒ ░     ▓██ ░▒░     ░ ▒░  ░ ░░▒░ ░ ░  ▒ ░░░▒ ▒ ░ ▒
░  ░  ░  ░░       ▒ ▒ ░░        ░   ░  ░░░ ░ ░  ▒ ░░ ░ ░ ░ ░   Versão: full
      ░           ░ ░            ░       ░      ░    ░ ░
                  ░ ░                              ░   \033[1;m

\033[31m▬▶ USER\033[1;m \033[33m%s\033[1;m \033[31mLOGGED!\033[1;m
""" %(usuario))

def Menu1():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Choose one of the options below to continue

\033[31m1\033[1;m) Start
\033[31m2\033[1;m) About
\033[31m3\033[1;m) Dependencies
\033[31m4\033[1;m) Permissions
\033[31m5\033[1;m) Levels

\033[31mq\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		Bloco1()
	elif opcao1 == "2":
		Sobre()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		Permissao()
	elif opcao1 == "5":
		MudarPara()
	elif opcao1 == "q":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to go back...\033[1;m ")
		Menu1()

def Permissao():
	Apresentacao()
	print("\n[\033[1;32m*\033[1;m] file to be applied to the permission.\n")
	sleep(3)
	os.system("ls | grep spyquiz.py | lolcat")
	sleep(3)
	print("\n[\033[1;32m*\033[1;m] Done, permissions applied.")
	sleep(3)
	os.system("chmod +x spyquiz.py")
	Menu1()

def MudarPara():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] Do you want to go to what level?

\033[31m01\033[1;m) Level - #1: Decryption
\033[31m02\033[1;m) Level - #2: Reading source code (Programming)
\033[31m03\033[1;m) Level - #3: Notice
\033[31m04\033[1;m) Level - #4: QrCode
\033[31m05\033[1;m) Level - #5: Information Collection, Wordlist
\033[31m06\033[1;m) Level - #6: Using layers
\033[31m07\033[1;m) Level - #7: Steganography
\033[31m08\033[1;m) Level - #8: ASCII - Dec
\033[31m09\033[1;m) Level - #9: Base64
\033[31m10\033[1;m) Level - #10: Binary
\033[31m11\033[1;m) Level - #11: Spectogram
\033[31m12\033[1;m) Level - #12: Mathematics
\033[31m13\033[1;m) Level - #13: Read the statement
\033[31m14\033[1;m) Level - #14: Octal
\033[31m15\033[1;m) Level - #15: Hexa
\033[31m16\033[1;m) Level - #16: Reverse
\033[31m17\033[1;m) Level - #17: Japa
\033[31m18\033[1;m) Level - #18: X of the question
\033[31m19\033[1;m) Level - #19: Turn around
\033[31m20\033[1;m) Level - #20: Browsing
\033[31m21\033[1;m) Level - #21: Arabica2rs
\033[31m22\033[1;m) Level - #22: Tigo3fx
\033[31m23\033[1;m) Level - #23: Atom128
\033[31m24\033[1;m) Level - #24: Dark
\033[31m25\033[1;m) Level - #25: Working and decrypting
\033[31m26\033[1;m) Level - #26: <i>
\033[31m27\033[1;m) Level - #27: Nazca Lines
\033[31m28\033[1;m) Level - #28: The Matrix
\033[31m29\033[1;m) Level - #29: Adam Smith
\033[31m30\033[1;m) Level - #30: The End

\033[31mq\033[1;m) Back
""")
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "01":
		Bloco1()
	elif opcao1 == "02":
		Bloco2()
	elif opcao1 == "03":
		Bloco3()
	elif opcao1 == "04":
		Bloco4()
	elif opcao1 == "05":
		Bloco5()
	elif opcao1 == "06":
		Bloco6()
	elif opcao1 == "07":
		Bloco7()
	elif opcao1 == "08":
		Bloco8()
	elif opcao1 == "09":
		Bloco9()
	elif opcao1 == "10":
		Bloco10()
	elif opcao1 == "11":
		Bloco11()
	elif opcao1 == "12":
		Bloco12()
	elif opcao1 == "13":
		Bloco13()
	elif opcao1 == "14":
		Bloco14()
	elif opcao1 == "15":
		Bloco15()
	elif opcao1 == "16":
		Bloco16()
	elif opcao1 == "17":
		Bloco17()
	elif opcao1 == "18":
		Bloco18()
	elif opcao1 == "19":
		Bloco19()
	elif opcao1 == "20":
		Bloco20()
	elif opcao1 == "21":
		Bloco21()
	elif opcao1 == "22":
		Bloco22()
	elif opcao1 == "23":
		Bloco23()
	elif opcao1 == "24":
		Bloco24()
	elif opcao1 == "25":
		Bloco25()
	elif opcao1 == "26":
		Bloco26()
	elif opcao1 == "27":
		bloco27()
	elif opcao1 == "28":
		Bloco28()
	elif opcao1 == "29":
		Bloco29()
	elif opcao1 == "30":
		Bloco30()
	elif opcao1 == "q":
		Menu1()
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to go back...\033[1;m ")
		MudarPara()

def Instalacao():
	def ArchDerivados():
		print("\n[\033[1;32m*\033[1;m] Please wait while we install the dependencies...\n")
		sleep(3)
		os.system("sudo pacman -S --noconfirm sl curl lolcat")
		print("\n\n[\033[1;32m*\033[1;m] Successfully installed.")
		input("\n\033[1;36mPress ENTER to go back...\033[1;m ")
		Menu1()
	def DebianDerivados():
		print("\n[\033[1;32m*\033[1;m] Please wait while we install the dependencies...\n")
		sleep(3)
		os.system("sudo apt install -y sl curl")
		print("")
		os.system("gem install lolcat")
		print("\n\n[\033[1;32m*\033[1;m] Successfully installed.")
		input("\n\033[1;36mPress ENTER to go back...\033[1;m ")
		Menu1()
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Choose your current distribution for the installation of the requirements.

\033[31m1\033[1;m) Arch Linux & Derivatives
\033[31m2\033[1;m) Debian & Derivatives
\033[31m3\033[1;m) Back
\033[31m4\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		ArchDerivados()
	elif opcao1 == "2":
		DebianDerivados()
	elif opcao1 == "3":
		Menu1()
	elif opcao1 == "4":
		exit(1)
	else:
		ComandoNaoEncontrado()


def Bloco1():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #1: Decryption
 ____________________________________________
|                                            |
|      23a37c7340995c9192471ce06ae4c3e8      |
|____________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "5950c237124755f423d01812a1dbe8281513adc0cfe3fa0a0bc984cefb381f7e13f91e8360716ffe78d77aa447c17c98ee77e23e495c496b0c8b8167cb177b9b"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco1()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco2()
	elif opcao1 == "2":
		Bloco2()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco1()

def Bloco2():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #2: Reading source code (Programming)
 ______________________________________________________________________________________________
|                                                                                              |
|      We will present a source code of a specific webpage within my site                      |
|                                                                                              |
|             You will have to find the password to pass, and go to the next level.            |
|______________________________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		print("""\033[35m

 █    ██  ██▀███   ██▓          ██▓███ ▓██   ██▓
 ██  ▓██▒▓██ ▒ ██▒▓██▒         ▓██░  ██▒▒██  ██▒
▓██  ▒██░▓██ ░▄█ ▒▒██░         ▓██░ ██▓▒ ▒██ ██░
▓▓█  ░██░▒██▀▀█▄  ▒██░         ▒██▄█▓▒ ▒ ░ ▐██▓░
▒▒█████▓ ░██▓ ▒██▒░██████▒ ██▓ ▒██▒ ░  ░ ░ ██▒▓░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ 
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░ ░▒  ░▒ ░     ▓██ ░▒░ 
 ░░░ ░ ░   ░░   ░   ░ ░    ░   ░░       ▒ ▒ ░░  
   ░        ░         ░  ░  ░           ░ ░     
                            ░           ░ ░\033[1;m

""")
		print("\033[31mWait\033[1;m\033[32m...\033[1;m")
		sleep(2)
		os.system("curl https://sup3r-us3r.github.io/spyquiz/level2.txt")
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "3250d88f8bd55e62ae3f769b9bdce1854bac2f645da0a982e6c68e2884c87b2b7d0bf62da7c3b21aa4d426d6d5223c111646f05f4fbdc7a4b6fafe1b6ad25823"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco2()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco3()
	elif opcao1 == "2":
		Bloco3()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco2()

def Bloco3():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #3: Notice

[\033[1;91m!\033[1;m] NOTE: This level requires that you have installed the dependencies!
If you have installed, proceed, if you do not go to option 3
 _________________________________________________________
|                                                         |
|The password is in the animation of the sign of the train|
|_________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Install the dependencies
\033[31m4\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		print("\n[\033[1;32m*\033[1;m] Warning, the Train will pass!")
		sleep(3)
		os.system("sl -a")
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b3fb9eb1b2749efa02c7d4d94df6f6ee7d2f7492e0482c46e2ee2716fb41de4bb3f4e9ab9e5bbe26ec9b2f34b0801a151e761063599c8904021b7328881e15b8"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco3()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")	
		Bloco4()
	elif opcao1 == "2":
		Bloco4()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco3()

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Sorry, the command was not found.
[\033[1;91m!\033[1;m] If the problem persists, tell the developer.
		''')

def Bloco4():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #4: QrCode
 _________________________________________________________________________
|                                                                         |
|        QrCode = https://sup3r-us3r.github.io/spyquiz/level4.png         |
|_________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "0ceeb7a66858efeb21bfb43f5b44d79420d443c28b8cc48c522c981e5ac98d47202add62649719d1307c5baa44a6de4c4b6bcaeb1875a7bd94854b1810125502"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco4()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco5()
	elif opcao1 == "2":
		Bloco5()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco4()

def Bloco5():
	Apresentacao()
	lista = []
	i = 1
	print('''
[\033[1;32m*\033[1;m] Level - #5: Information Collection, Wordlist
 _________________________________________________
|                                                 |
|Robert D. Baker                                  |
|Girlfriend: Ketty                                |
|Music style: Electronic                          |
|City: New York                                   |
|Mother's name: Marta                             |
|Father's name: Peterson                          |
|Grographic coordinates: 43,010354, -88,076145    |
|Telephone: 414-557-3179                          |
|City Code: 55                      	          |
|Date of birth: July 20, 1982                     |
|Age: 34 years old                                |
|Sign: Leo                                        |
|E-mail Address: robertdbaker@gmail.com           |
|User Name: bakerdr                               |
|MasterCard: 5159 6656 3798 1026                  |
|Conceded: 6/2018                                 |
|Dog Name: titicozito                             |
|Company: Robotic Solution                        |
|Occupation: Robotica                             |
|Height: 1,75                                     |
|Weight: 78 Kg                                    |
|Blood type: B+                                   |
|Favorite color: Green                            |
|Vehicle: Ninja H2R                               |
|_________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		try:
			Reply = int(input("\n\033[1;36mPlace the number of passwords you want to import into your wordlist (ex: 5):\033[1;m "))
			print("\n")
			print("[\033[1;91m!\033[1;m] NOTE: Enter the passwords that can be the one of the victim, according to the data informed above.\033[1;m")
		except:
			print("\n[\033[1;91m!\033[1;m] Wrong value!")
			sleep(2)
			return Bloco5()
		while i <= int(Reply):
			nomes_das_senhas = input("\n\033[1;36mPassword #\033[1;m"+ str(i) +": ")
			lista.append(nomes_das_senhas)
			if nomes_das_senhas == "bakerdr20071982":
				print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
				input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
				Bloco6()
				break
			i += 1

		else:
			print("[\033[1;91m!\033[1;m] Incorrect response.")
			input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
			Bloco5()
	elif opcao1 == "2":
		Bloco6()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco5()

def Sobre():
	Apresentacao()
	print('''

╔════════════════════════════════════════╗
║ \033[31m⟫\033[1;m\033[33m⟫\033[1;m\033[32m⟫\033[1;m \033[1m\033[37mSobre\033[1;m                              ║
║                                        ║
║ Nome do Programa: \033[32mSpy-Quiz\033[1;m             ║
║ Data de Criação: \033[32m04/11/2016\033[1;m\033[1;m            ║
║ Versão: \033[32mfull\033[1;m                           ║
║ Desenvolvedores: \033[32mSup3r-Us3r\033[1;m \033[31m-\033[1;m \033[32mf1v5\033[1;m     ║
╚════════════════════════════════════════╝
╔═════════════════════════════════════════════════════════════════════════╗
║ \033[31m⟫\033[1;m\033[33m⟫\033[1;m\033[32m⟫\033[1;m \033[1m\033[37mDescrição\033[1;m                                                           ║
║                                                                         ║
║ Ferramenta desenvolvida com o propósito de testar suas habilidades.     ║
╚═════════════════════════════════════════════════════════════════════════╝
╔═════════════════════════════════════════════╗
║ \033[31m⟫\033[1;m\033[33m⟫\033[1;m\033[32m⟫\033[1;m \033[1m\033[37mSup3r-Us3r\033[1;m                              ║
║                                             ║
║ [SITE]: \033[32mhttps://sup3r-us3r.github.io\033[1;m        ║
║ [GITHUB]: \033[32mhttps://github.com/Sup3r-Us3r\033[1;m     ║
║ [YOUTUBE]: \033[32mhttps://youtube.com/MagnoTutor\033[1;m   ║
╚═════════════════════════════════════════════╝
''')
	input("\n\033[1;36mPress ENTER to go back...\033[1;m ")
	Menu1()

def Bloco6():
	login = True
	senha = True
	q1 = False
	q2 = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #6: Using layers
 _____________________________________________________________
|                                                             |
|     The login and password is in the file "level6.psd"      |
|                                                             |
|        http://sup3r-us3r.github.io/spyquiz/level6.psd       |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while login != q1 and senha != q2:
			login = input("\n\033[1;32m[*] Login: \033[1;m")
			login = hashlib.sha512(login.encode('utf-8'))
			login = login.hexdigest()
			senha = input("\033[1;32m[*] Password: \033[1;m")
			senha = hashlib.sha512(senha.encode('utf-8'))
			senha = senha.hexdigest()
			q1 = "5667ae23cdbefe166f2e06d442375516cfaaad6aa1363f941309ec1aa1d130bfb33a32a5419a9093ab037881016f66c6796f16f4a2d5be6fb647aa9a56dec303"
			q2 = "985aa195c09fb7d64a4bb24cfe51fb1f13ebc444c494e765ee99d6c3ef46557c757787f8f5a6e0260d2e0e846d263fbfbe1311c884bb0bf9792f8778a4434327"
			if login != q1 or senha != q2:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco6()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco7()

	elif opcao1 == "2":
		Bloco7()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco6()

def Bloco7():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #7: Steganography
 _________________________________________________________________
|                                                                 |
|           The password is inside the "spypass.png" image        |
|                                                                 |
|        https://sup3r-us3r.github.io/spyquiz/level7.jpg          |
|_________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "2c0f3ada9e5d314d9c5a37dc638a6df186882c492c179ea746b63d053a7cef558b2ae3876eff556c82fe2c0ce232c8b576b52b4efcd6209c1f35ff49c2825e58"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco7()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco8()
	elif opcao1 == "2":
		Bloco8()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco7()

def Bloco8():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #8: ASCII - Dec
 ______________________________________________________________________________
|                                                                              |
|                           Find the password...                               |
|                                                                              |
|      | (35) | (83) | (112) | (121) | (65) | (83) | (67) | (73) | (73) |      |
|______________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "cd0eca5dbd9e4d6534854807b48aa1a3acb254031756ce281194228d3c6d892058f150d24b2e4cd643248ca3bb41a136da2109245dae985bd126016759c065db"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco8()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco9()
	elif opcao1 == "2":
		Bloco9()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco8()

def Bloco9():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #9: Base64
 ____________________________________________
|                                            |
|      YmFzZTY0LWRlY29kZS1zdWNjZXNzZnVs      |
|____________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "1d427a35aedcdc4fcf5bb729d46a00c3ce5d7832640fcfe70d97a84dc22fc2d53e35571a8fbf6085941e73b5fbd7af06d7c289a35fac59f1d62374cc442e3358"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco9()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco10()
	elif opcao1 == "2":
		Bloco10()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco9()

def Bloco10():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #10: Binary
 ________________________________________________________
|                                                        |
|      01100100 01101001 01100110 01100110 01101001      |
|      01100011 01110101 01101100 01110100 00111111      |
|________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "a816208946c8aa49ab6f60afbd372a12ca4d95ac58f22edcb21bc87ad19186569d31610086b626266b18d2426d2705651731771353d8c0e0967955cddc2adc9a"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco10()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco11()
	elif opcao1 == "2":
		Bloco11()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco10()

def Bloco11():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #11: Spectogram
 __________________________________________________________________________
|                                                                          |
|      Make a spectogram in the file "hex.wav" to find the answer          |
|                                                                          |
|       Para ouvir: https://sup3r-us3r.github.io/spyquiz/level11.wav       |
|__________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "211824f7f2736ce7e4acfa07649561188fbd0c39de4f5fd20483c6bb15f327146086b62edefb8e7213b2a2eda07720786b4587e97856c22904f7f175b1e40fbe"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco11()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco12()
	elif opcao1 == "2":
		Bloco12()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco11()

def Bloco12():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #12: Mathematics
 _________________________________________________________________________
|                            |                                            |
|      M + M + M = 1080      |      E + 3rd Term of PG (2,4,...) = I      |
|                            |                                            |
|      M + A + A = 1314      |      I + Log4 64=x                         |
|                            |____________________________________________|
|      A + T + T = 511       |                                            |
|                            | Hint:                                      |
|      A + T x M = E         |      print("Find the final answer :D")     |
|____________________________|____________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "a81af4e6fada061924e905358091bca96af72705a2177b78dda9032b75b1668aa1dd09ae0d986c33bd594102a2241933a9594268717869d3d1b0730c52866faf"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco12()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco13()
	elif opcao1 == "2":
		Bloco13()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco12()

def Bloco13():
	p = True
	q1 = False
	q2 = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #13: Read the statement
 ____________________________________________________
|                                                    |
|   The password for the next level is: embinario    |
|____________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q1 and p != q2:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q1 = "e59d0329d6c9e23abc8b287107ddc9281defff1af776133ed618859da59b63c943b019f7603d8344d8eb2d36851234a59c75afa70c1d317fd7676c22e3f5c71f"
			q2 = "452f7d4966a7815f665b4f97204331e114063251ef90ac4c19732fbd54977a5c1a159b04c903e918c755bbc475ab4acf239f9e1ee8ce801329b878c53229bd41"
			if p != q1 and p != q2:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco13()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco14()
	elif opcao1 == "2":
		Bloco14()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco13()

def Bloco14():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #14: Octal
 _______________________________________________________
|                                                       |
|    The password for the next level is: octaleumadlç   |
|_______________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "73229a1024cec29476fd179cb89b1abf74d0b6cc028976a1a62cd9477f8bcdb6fca37fa428c5558ecf5218f112cb7ff2b05833c88f4a736a3f8a531a640753ad"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco14()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco15()
	elif opcao1 == "2":
		Bloco15()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco14()

def Bloco15():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #15: Hexa
 ______________________________________________________________________
|                                                                      |
|   The password for the next level is: ta_achando_facil_ne_moleque    |
|______________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "a5614ff46a800ce96fe21c00173a12006a92653088fc0d354df738da404ddacda51d73d20a135194fafdfa7c9f2e119b0dffe68337733b0bf54838558302dd7e"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco15()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco16()
	elif opcao1 == "2":
		Bloco16()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco15()

def Bloco16():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #16: Reverse
 _______________________________________________________________________________
|                                                                               |
|      See you for just wait - still a lot of help will tool you This           |
|_______________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "c620998bead50e43a9298325a6fa11518afe66035741b98e34b85d967750f7b12c0d710248cf40943906bb5c0b225fb4b959c59f050f975feadfa3ba9e206df1"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco16()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco17()
	elif opcao1 == "2":
		Bloco17()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco16()

def Bloco17():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #17: Japa
 _________________________________________________________________________________
|                                                                                 |
|      This time things will change, find the password that is encrypted          |
|_________________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		print("")
		print("\033[31mAguarde até a senha criptografada aparecer\033[1;m\033[32m...\033[1;m")
		sleep(3)
		print("")
		os.system("curl https://raw.githubusercontent.com/Sup3r-Us3r/sup3r-us3r.github.io/master/spyquiz/level17.txt")
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "4df1510bbaab42cccd08bed15a439bd1baf1aee48dbd5b7165bf4de3e90636778fef155a078cf9b3885c84d0cd2d51a274476f47a2d97017467ee4eca6167c76"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco17()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco18()
	elif opcao1 == "2":
		Bloco18()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco17()

def Bloco18():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #18: X of the question
 ________________________________________
|                                        |
|      A*5 - B^7 + C%2 + D sin 3214      |
|                                        |
|      A=15  B=12  C=7   D=13            |
|________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "84b214c42250dbcb999167a5aa9f240d805655a8fca7574d7c7e18682e85b0ad0e643ca5a7c3e18871259b69a85519a2d62b9a7d9edc2105139b296bcbe9effe"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco18()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco19()
	elif opcao1 == "2":
		Bloco19()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco18()

def Bloco19():
	p = True
	q1 = False
	q2 = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #19: Turn around
 ______________________________________________________________________________________________________________
|                                                                                                              |
|      ... ..- .- / ... . -. .... .- / . / -- --- .-. ... . -.-. --- -.. . -. . -..- - .-.. . ...- . .-..      |
|                                                                                                              |
|      To listen: https://sup3r-us3r.github.io/spyquiz/level19.wav                                             |
|______________________________________________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q1 and p != q2:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q1 = "f30c7b68f3b8624dc10080a80f1dde2e68643bf7d47dc75ec71e5980178b91ffa74ba53e1c0b26bbacc8130ca594787a697ba2eb33d748db89df78aa941d1d79"
			q2 = "b437f52e979bb57f95f5a67b68d604e6b83d972ba476f95ea0a483c0631ccfa535ca3761cb88f427b5cbcae902401c33d3f68f27b1c8d80523f0fd57fcc30302"
			if p != q1 and p != q2:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco19()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco20()
	elif opcao1 == "2":
		Bloco20()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco19()

def Bloco20():
	login = True
	senha = True
	q1 = False
	q2 = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #20: Browsing

[\033[1;91m!\033[1;m] OBS: The game is turning is not really, we started from below and we are going up.
 _______________________________________________________________________
|                                                                       |
|      Find the login and password that is somewhere on my site ;)      |
|                                                                       |
|      https://sup3r-us3r.github.io/spyquiz/level20.html                |
|_______________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while login != q1 and senha != q2:
			login = input("\n\033[1;32m[*] Login: \033[1;m")
			login = hashlib.sha512(login.encode('utf-8'))
			login = login.hexdigest()
			senha = input("\033[1;32m[*] Senha: \033[1;m")
			senha = hashlib.sha512(senha.encode('utf-8'))
			senha = senha.hexdigest()
			q1 = "c7809fd363e6dc44fb735fd086ea623fae16762c79d4c810e5d9fc1d7514b5d1ed1f646c042f3cd131fe90cd774b029e7a64904a969cd77c0dcb9e58e4134630"
			q2 = "497fe595951961337b77f1188333992ea20fe1c0faf1fdfe484613e0462b343fdea3d3752489b1392cff0e38310aa9133c4de9c2651bef731fec59a8a2f0a107"
			if login != q1 or senha != q2:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco20()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco21()
	elif opcao1 == "2":
		Bloco21()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco20()

def Bloco21():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #21: Arabica-2rs
 _______________________________________________________________________
|                                                                       |
|                           Find the password...                        |
|                                                                       |
|      ىﺿ أﺹ طبنرغﺿ أﺹ ﺿ ی ا ﺿىة ﺿ اىﺿأﺹحغ كز بن ح ب ﻑحغكزب ن ح بش      |
|_______________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "3ff7b5f3519791e03cbfde2c667189e32b5a1de1df7781dc6a99110621b311f94a0b4fa6c3456e5e60af911fc1d6da18a7e09cf6606a7e4f6ffb8b80c39eae63"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco21()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco22()
	elif opcao1 == "2":
		Bloco22()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco21()

def Bloco22():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #22: Tigo3fx
 ________________________________________________________________________________________________
|                                                                                                |
|      W/+Ow8Df=0YYt1VMcAzOm/+OwALfwdrMcb4AwRYh=kLfwdrot+4yB049t1VMt++Tt1Drt1VM1lVoc0Pb=RWX      |
|________________________________________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "7986ea8b0a90a4d804bdf5be1dbf20f197594bd265605d0c6122ffc83e365ff93b2bf50532380a1ffd0db37b03ea30f1500b7bc19cb90d5915996cebeb8ab4fc"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco22()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco23()
	elif opcao1 == "2":
		Bloco23()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco22()

def Bloco23():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #23: Atom128
 ___________________________________________________________________
|                                                                   |
|     The password for the next level is 15 times the decryption    |
|___________________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		print("")
		os.system("curl https://raw.githubusercontent.com/Sup3r-Us3r/sup3r-us3r.github.io/master/spyquiz/level23.txt | lolcat")
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b3efba35d9f9249c2d9bd51311ac60a7d1c9cd46c6aef60b03798f250ae708dfea06ab31d323e274380f5fe7138d01dc651a7bc95cf8d0599fb188e872c88c70"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco23()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco24()
	elif opcao1 == "2":
		Bloco24()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco23()

def Bloco24():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #24: Dark
 _____________________________________________________________
|                                                             |
|                         It's Dark!                          |
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level24.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "96f4aab59ec41e6ccf0f7900110605e1a862ee88cdfe6b15e12f2279802e74825eee87185a2f171eadde5af71edfbcc2bc05de8d307030970ac69496343b27c0"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco24()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco25()
	elif opcao1 == "2":
		Bloco25()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco24()

def Bloco25():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #25: Working and decrypting
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level25.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "8c865996b232749856eaaa84beca73f7f7899c0f5b156c1937e5fbe00da2fdc622189f668e55bdced8ed0776e8e2a67635199caabaef9f079c050d617f04ff07"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco25()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco26()
	elif opcao1 == "2":
		Bloco26()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco25()

def Bloco26():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #26: <i>
 ______________________________________________________________
|                                                              |
|      https://sup3r-us3r.github.io/spyquiz/level26.html       |
|______________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b2f94334d36dc26df98176c80a9a91678fbf094d8062008625e86f351feac9de953f5c56c54a208ae7c24856846a090ec00eb3b3c44eaad9edd2d54a8c860ac1"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco26()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco27()
	elif opcao1 == "2":
		Bloco27()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco26()

def Bloco27():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #27: Nazca Lines
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level27.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "3aa3c49aa5bd035ced20abdc76c69115d650bb79bed7310ebdc4a5af75910bfa5fd2f687118821b533b39d3c680530ef77d0c1aea1c9ea3d1e0c74c67b0d8f4b"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco27()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco28()
	elif opcao1 == "2":
		Bloco28()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco27()

def Bloco28():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #28: Matrix
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level28.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "66ebd76cff37004213b5ffcbd4020c269c27652a133d95bfbcc5c151b38871d0279946470f21ed84513762677404ab4931cd300c761ad9f50a1ce76a40188df1"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco28()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco29()
	elif opcao1 == "2":
		Bloco29()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco28()

def Bloco29():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #29: Adam Smith
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level29.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "cebfea666f6685057dedccfaa31238068ae56c7e465fec31835d8e320a17caf268f0a303f6d109b7484cbe2522c4806106d589c6b252f4e46a219e5318afaa40"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco29()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Bloco30()
	elif opcao1 == "2":
		Bloco30()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco29()

def Bloco30():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Level - #30: The End
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level30.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Reply
\033[31m2\033[1;m) Skip
\033[31m3\033[1;m) Exit
''')
	opcao1 = input("\033[1;36mOption:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mReset: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "30161ddbc5c1a80f90e37350b3e0f937902330ed9a4431143dd02690ddfe343eac7abd7066be22959bfeed91870d5ac85f3fe5f89f2d5b87c939f71ae4bbc121"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Incorrect response.")
				input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
				Bloco30()
		print("\n\033[1;32m[*] Correct answer!\033[1;m\n")
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		os.system(Limpar)
		FimDoDesafio()
	elif opcao1 == "2":
		os.system(Limpar)
		FimDoDesafio()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPress ENTER to try again...\033[1;m ")
		Bloco30()

def FimDoDesafio():
	try:
		print(""" \033[31m
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████  ██▀███      ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒   ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ▓██ ░▄█ ▒   ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄     ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░     ░░   ░    ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░   ░            ░ ░        ░     ░  ░   ░
                                                              ░ \033[1;m

\033[31m▬▶ END OF QUIZ, THANK YOU\033[1;m \033[33m%s\033[1;m \033[31mFOR TRYING THIS HACKER CHALLENGE!\033[1;m

\033[45m
╔═══════════════════════════════════════════════╗
╠═ If you fall, get up                          ║
╠═ Sliding will hold                            ║
╠═ But never think about giving up              ║
╠═ Because how much more bitter is your fall    ║
╠═ But sweet will be your victory               ║
╚═══════════════════════════════════════════════╝\033[1;m
""" %(usuario))
		input("\n\033[1;36mPress ENTER to continue...\033[1;m ")
		Sobre()
	except:
		exit(1)

Menu1()
