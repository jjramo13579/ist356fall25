
# Challenge 1-2-1

'''
Write a program to accept a password as input. If the password input is "secret" display "access granted" else say "invalid password"

repeat the above up to 5 times. when the correct password is entered, stop looping when 5 loops have exhaused print "you are locked out"

'''

valid_pw = "secret"

for i in range(5):
    pw = input("Enter password")
    if pw == valid_pw:
        print("access granted")
        break
    else:
        print("invalid password")
else:
    print("you are locked out")