def loginValidation(username:str, password:str) -> int:
    attempts = 0

    while attempts != 3:
        usrInputUsername = input("Please Enter The Username: ")
        usrInputPassword = input("Please Enter The Password: ")

        if usrInputUsername != username or usrInputPassword != password:
            attempts += 1
            print("Username or Password is incorrect. Please Try Again.")
        else:
            print("Login Successful")
            return 0

    print("Too many attempts")

userName = "iDunno"
password = "password"
loginValidation(userName, password)
