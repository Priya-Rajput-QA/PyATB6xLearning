"""Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"""

username = input("Enter your username:").strip()
password = input("Enter your password:").strip()

if username=="admin" and password=="1234":
    print("Login successfully")
else:
    print("Invalid Credentials")




