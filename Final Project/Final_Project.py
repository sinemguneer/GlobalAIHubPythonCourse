import pandas as pd
import csv

data = pd.read_csv("project.csv")
trueCounter = 0

for i in range(10):
    questions = data.values[i][0]
    print(questions)
    answer = input("Answer : ")
    if answer == data.values[i][1]:
        trueCounter += 1

if trueCounter <= 5 :
    print("Point = ",trueCounter*10)
    print("Unsuccessful")
else:
    print("Point = ", trueCounter * 10)
    print("Successful!")