
def encrypt(string2,key):
	result = ""
	
	for i in range(len(string2)):
		char=string2[i]
		#print(char)

		if(char.isupper()):
			result=result+chr((ord(char) + key - 65 ) % 26 + 65 )
		if(char.islower()):
			result=result+chr((ord(char) + key - 97 ) % 26 + 97 )
	return result

def decrypt(cipher,key):
	result=""

	for i in range(len(cipher)):
		char=cipher[i]
		
		if(char.isupper()):
			result=result+chr((ord(char) - key - 65 ) % 26 + 65)
		if(char.islower()):
			result=result+chr((ord(char) - key - 97 ) % 26 + 97 )
	return result

def bruteforce(cipher):
	
	for key in range(0,26):
		result=""
		for i in range(len(cipher)):
			char=cipher[i]
		
			if(char.isupper()):
				result=result+chr((ord(char) - key - 65 ) % 26 + 65)
			if(char.islower()):
				result=result+chr((ord(char) - key - 97 ) % 26 + 97 )
		
		print("Using Key #",key,": ",result)


print('''Enter Choice:
	1:Encrypt
	2:Decrypt
	3:Brute Force
	Other key:Exit''')
ch=int(input())
if(ch==1):
	string1=input("Text:")
	key=int(input("Shift Key:"))
	cipher=encrypt(string1,key)	
	print("cipher:",cipher)

elif(ch==2):
	cipher=input("Cipher Text:")
	key=int(input("Shift Key:"))
	plaintext=decrypt(cipher,key)
	print("Plaintext:",plaintext)
elif(ch==3):
	cipher=input("Cipher Text:")
	bruteforce(cipher)
else:
	exit(0)

