correct_username_jbgp = "admin"
correct_password_jbgp = "1234"
attempts_jbgp = 0

while attempts_jbgp < 3:
    userName_jbgp = input("Enter username: ")
    password_jbgp = input("Enter password: ")
    
    if userName_jbgp == correct_username_jbgp and password_jbgp == correct_password_jbgp:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_jbgp += 1

if attempts_jbgp == 3:
    print("Account Locked")

