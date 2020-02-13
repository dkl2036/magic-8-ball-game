import random
import time

print("Ask Python, the Magic 8 Ball a question!")

time.sleep(5) # waits 5 seconds

print("Searching for an answer . . . ")

time.sleep(2) # waits 2 seconds

print("Please be patient . . .")

time.sleep(1) # waits 1 seconds

for dot in range(10): # prints 10 dots seperated by 0.5 pause 
    print(".")
    time.sleep(0.5) # waits 0.5 seconds

time.sleep(1) # waits 1 seconds

print("Python, the magic 8 ball says . . .")

time.sleep(3) # waits 3 seconds

answer = random.randint(1,9) # generates random number for answer in range

if answer == 1:
    print("As I see it, yes.")

elif answer == 2:
    print("Ask again later.")

elif answer == 3:
    print("Better not tell you now.")

elif answer == 4:
    print("Yes – definitely.")

elif answer == 5:
    print("Without a doubt.")

elif answer == 6:
    print("Outlook not so good.")

elif answer == 7:
    print("Reply hazy, try again.")

elif answer == 8:
    print("My sources say no.")

elif answer == 9:
    print("Concentrate and ask again.")
    
