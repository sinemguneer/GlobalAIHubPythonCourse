#Explain your work

#Question 1

userInfo = {"userName":['global','admin'],"password":['123','admin']}

username = input("Please enter your username : ")
password = input("Please enter your password : ")
for i in range(len(userInfo["userName"])) :
	if username == userInfo["userName"][i] :
		if password == userInfo["password"][i]:
			print("Successfully Login!")
		else:
			print("Login Failed!!")