#!/usr/bin/python
#v0.0.0.1
import requests
import getpass
ktf = requests.Session()

usrlist_base = "http://www.klartraumforum.de/forum/memberlist.php?sort=postnum&order=desc&perpage=500&page="

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
boards = {
	"Fragen & Antworten":[
		"Anfaengerbereich",
		"Klartraeume",
		"Techniken",
		"Hilfsmittel",
		"Dachboden"
		],
	"Erlebnisse":[
		"Experimente im Klartraum",
		"Klartraumberichte",
		"Normale Traeume",
		"Ziele im Klartraum",
		"Basale Klarheit",
		"Persoenliche Logbuecher",
		"Sonstige Erlebnisse"
		],
	"Mentoring und Arbeitsgruppen":[
		"Mentoring",
		"Arbeitsgruppen"
		],
	"Community":[
		"Traeumer stellen sich vor",
		"Klartraumtreffen",
		"Literatur, Web & Sonstiges",
		"Speakers Corner",
		"Kreatives",
		"Philosophisches"
		],
	"Sonstiges":[
		"Ankuendigungen",
		"Kritiken und Anregungen"
		]
}

def login(usr, pw):
	payload = {
		"action":"do_login",
		"url":"http://www.klartraumforum.de/forum/index.php",
		"quick_login":"1",
		"quick_username":usr,
		"quick_password":pw
	}
	resp = ktf.post("http://www.klartraumforum.de/forum/member.php", payload)
	if resp.text.encode("utf8").find("Bitte korrigiere die folgenden Fehler") != -1:
		return False
	else:
		return True
		
def clear():
	import os
	os.system("clear")
	
def reply():
	tidnum = raw_input("Number of thread: ")
	if tidnum != "":
		try:
			tidnum = int(tidnum)
		except:
			print "ERROR."
			return false
	else:
		print "ERROR."
		return false
	import os
	os.system("nano Antwort_schreiben.txt")
	try:
		open("Antwort_schreiben.txt").read()
	except:
		return False
	
def findUsrId():
	usrName = raw_input("Username > ")
	resp = ktf.get(usrlist_base + "1").text
	
	
def change_board(com):
	pass


usr_u = raw_input("%sPlease log in.\nUsername > %s"%(bcolors.OKBLUE, bcolors.ENDC))
pwd_u = getpass.getpass("%sPassword(input will be hidden) > %s"%(bcolors.OKBLUE, bcolors.ENDC))
if (login(usr_u,pwd_u)):
	print("%sSuccess!%s"%(bcolors.OKGREEN,bcolors.ENDC))
	urlstr = "~"
	while 1:
		com = raw_input("%s%s@klartraumforum.de%s:%s~%s$ "%(bcolors.BOLD+bcolors.OKGREEN,usr_u,bcolors.ENDC,bcolors.BOLD+bcolors.OKBLUE,bcolors.ENDC))
		if com == "clear":
			clear()
		elif com == "reply":
			reply()
		elif com == "usrId":
			findUsrId()
		elif com[:3] == "cd ":
			change_board(com)
		else:
			print("%sERR: Command \"%s\" not recognized.%s"%(bcolors.FAIL + bcolors.BOLD, com, bcolors.ENDC))
else:
	print("%sSomething was wrong. Please try again.%s"%(bcolors.FAIL + bcolors.BOLD,bcolors.ENDC))
