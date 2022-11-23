username = input()
password = input()

while True:
    typed_pass = input()
    if typed_pass == password:
        print(f'Welcome {username}!')
        break
