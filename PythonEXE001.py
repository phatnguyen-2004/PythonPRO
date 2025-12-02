password = "beAwesome0301@"
count = 0
while count < 3:
    user = input(f"Enter your password : ")
    if user == password:
        print("Correct password ✅")
        break
    else:
        print("Incorrect password ❌")
        count += 1
else:
    print("Password entry failed ❌")