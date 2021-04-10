#Explain your work

#Question 1
dict = {"global" :"123","admin":"admin"}
username = ""
password = ""

def check(username, password):
	username = input("Username :")
	password = input("Password :")

	if username in dict.keys() and password in dict.values():
		print("Successfully Login!")
	else:
		print("Login Failed!!")

check(username,password)