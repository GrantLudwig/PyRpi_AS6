# File Name: ludwig_grant_AS06.py
# File Path: /home/ludwigg/Python/PyRpi_AS6/ludwig_grant_AS06.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS6/ludwig_grant_AS06.py

# Grant Ludwig
# 10/16/2019
# AS.06
# Create a median function

# returns if number is odd or even
def odd(num):
	if num % 2 == 0:
		return False
	else:
		return True

# takes in a list of integers
def median(numList):
	sortedList = sorted(numList)
	if odd(len(numList)):
		return sortedList[int(len(numList)/2)] # returns middle number in list
	else:
		first = sortedList[(int(len(numList)/2)) - 1] # first middle number
		second = sortedList[int(len(numList)/2)] # second middle number
		return (first + second) / 2 # returns average of middle numbers
		
# main
userList = []
print("Enter a list of numbers to get the median. Enter q to stop adding numbers.")
num = ""
while(num != "q" and num != "Q"):
	num = input("Number: ")
	if num != "q" and num != "Q":
		userList.append(int(num))

print(median(userList))