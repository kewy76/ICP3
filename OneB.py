# Kate Williams
# 6/11/2018

theString = input("Enter your string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

x = 0
count = 0

while x < len(theString):
    if theString[x].lower() in vowels:
        count += 1
    x += 1

print("The count of vowels is " + str(count))
