import random

print('Welcome to Password generator ')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,/1234567890!@%^&*()_abcdefghijklmnopqrstuvwxyz'

number  = input('Amounts of passwords to generate: ')
number = int(number)

length = input('Your Password Length: ')
length = int(length)

print('\here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
 
print(passwords)