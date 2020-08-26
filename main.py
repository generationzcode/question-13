Registered = input("Are you registered with us?")
if Registered == "Y":
  username = input("user:")
  password = input("pass:")
elif Registered == "N":
  print("go to the registration page")
else:
  print("please try again. Input Y/N")
  