# Kate Williams
# 6/11/2018

theDict = {}

theString = input("Enter your string: ")

count = 0

for word in theString.split():
    if word not in theDict.keys():
        theDict[word] = 0
    theDict[word] += 1

print(sorted(theDict))