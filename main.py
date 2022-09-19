from hashlib import sha256, md5
import csv

def rightHash(frase, hash1, hash2):
	print("Testando a frase: '" + frase + "'\n")
	if sha256(frase.encode('utf-8')).hexdigest() == hash1:
		print("SHA256 correto.")
	else:
		print("SHA256 incorreto.")
	if md5(frase.encode('utf-8')).hexdigest() == hash2:
		print("MD5 correto.\n")
	else:
		print("MD5 incorreto\n")

with open('frases.csv') as csvfile:
	localfile = csv.reader(csvfile, delimiter='|')
	for row in localfile:
		rightHash(row[0], row[1], row[2])
