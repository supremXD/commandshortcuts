import os


def start():
	nombre = input("Name of the file ----> ")
	os.system("sudo cp "+nombre+" '/var/www/html/downloads'")
	while True:
		exit()
start()
