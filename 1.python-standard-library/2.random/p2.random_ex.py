import random

print(random.randrange(200))
print(random.randrange(14, 20))
print(random.randrange(9, 20, 3))
print(random.randint(14, 20))


import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
print(password)
