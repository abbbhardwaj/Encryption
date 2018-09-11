import random

chars = 'abcdefgh!@%^*&ijklmn1234567opqrstuvwxyzABHCDEFGHIJKLMNO0912345678!%@^$'

password = ''
length = 10

for c in range(length):
    password += random.choice(chars)
print(password)
