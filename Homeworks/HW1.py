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
