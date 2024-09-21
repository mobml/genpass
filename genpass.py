import string
import random
import pyperclip as clip
import sys

size = len(sys.argv)

if size == 0 or size == 1:
    print("No lenght provided")

else: 
    lenght = int(sys.argv[1])

    chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(chars) for i in range(lenght)) 

    print("password is: " + password) 
    clip.copy(password)