#Question 1
list = [1,2,3,4,5,6,"Global","AI","Hub"]

firstHalf = []
lastHalf =[]

for i in range(len(list)//2) :
	firstHalf.append(list[i])
for j in range(len(list)//2,len(list)):
	lastHalf.append(list[j])

lastHalf = lastHalf + firstHalf
print(lastHalf)

#Question 2
number = float(input("Please enter a single digit number : "))
list = []
if (number<0 or number>=10) or int(number)-number !=0  :
	while number<0 or number>=10 or int(number)-number !=0:
		number = float(input("Please enter a single digit number : "))

for i in range(0,int(number)+1):
	if i % 2 == 0:
		list.append(i)
print(list)
