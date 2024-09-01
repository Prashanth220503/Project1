import random

uppr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = uppr_letters.lower()
spec_chars = """~!@#$%^&*()_+"'-=}{[]:;?><,./"""
digits = "0123456789"

all_char = ""

upper = True
lower = True
nums = True
symbols = True

if upper:
    all_char += uppr_letters
if lower:
    all_char += lower_letters
if nums:
    all_char += digits
if symbols:
    all_char += spec_chars

Length = int(input("Enter the Length of the Password: "))
amount = 5

for i in range(amount):
    password = "".join(random.sample(all_char, Length))
    print("Generated Password:", password)