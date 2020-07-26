import sys, time
token = sys.argv[1]
print(token)
token_digits = [int(digit) for digit in token]
print(token_digits)

#Waiting for scrcpy server to boot completely
time.sleep(4)
print("server booted")
