import re

pword = input("Enter password: ")
nums = r'\d'
spec = r'[^a-zA-Z0-9\s]'


if pword in open('1000-most-common-passwords.txt').read():
    print("Password too common.")
    quit()

if len(pword) < 8:
    print("Password must be 8 characters or more.")
    quit()

else:
    if re.search(spec, pword) and re.search(nums, pword):
        sec = 'Secure password'
    elif re.search(nums, pword):
        sec = 'Medium password'
    else:
        sec = 'Weak password'
    print(sec)