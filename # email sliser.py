def main():
    print("welcome the email slicer")
    print("")

    email_input = input("input your email address: ")


    (username, domain) = email_input.split("e")
    (domain, extension) = domain.split(".")
    
    print("username: " + username)
    print("Domain : " + domain)
    print("Extention: " + extension)

while True:
    main()