#!/usr/bin/env python
# coding: utf-8

# #  MD5 Hashing

# #    Code When input is static

# In[1]:


import hashlib


# In[2]:


# working of MD5 (string - hexadecimal & string - byte)

# initializing string
md5_hash = "Rithik"

# encoding "Rithik" using encode()
# then sending to md5()

# printing the equivalent byte value.
result = hashlib.md5(md5_hash.encode())
print("The byte equivalent of MD5 hash is : ", end ="")
print(result.digest())

print('\n')

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 hash is : ", end ="")
print(result.hexdigest())


# #  Code When input is dynamic

# In[3]:


# working of MD5 (string - hexadecimal & string - byte)

# inputting string
md5_hash = input('Enter string to be converted to hash: ')

# encoding the inputted string 
result = hashlib.md5(md5_hash.encode())

# printing the equivalent byte value.

print("The byte equivalent of MD5 hash is : ", end ="")
print(result.digest())

print('\n')

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 hash is : ", end ="")
print(result.hexdigest())


# # SHA1 Hashing 

# In[4]:


# working of SHA1 (string - hexadecimal & string - byte)

import hashlib

# initializing string
sha1_hash = "Bruh!"

# encoding "Bruh!" using encode()
# then sending to SHA1()

# printing the equivalent byte value.
result = hashlib.sha1(sha1_hash.encode())
print("The byte equivalent of SHA1 hash is : ", end ="")
print(result.digest())

print('\n')

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 hash is : ", end ="")
print(result.hexdigest())


# # SHA512 Hashing

# In[5]:


# working of SHA512 (string - hexadecimal & string - byte)

import hashlib

# initializing string
sha512_hash = "ShapeAI"

# encoding "Bruh!" using encode()
# then sending to SHA512()

# printing the equivalent byte value.
result = hashlib.sha512(sha512_hash.encode())
print("The byte equivalent of SHA512 hash is : ", end ="")
print(result.digest())

print('\n')

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 hash is : ", end ="")
print(result.hexdigest())


# # Salting 

# * Salt is random data that is used as an additional input to a one-way function that hashes data, a password or passphrase. Salts are used to safeguard passwords in storage.

# In[6]:


import uuid
import hashlib
 
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You\'ve entered the right password')
else:
    print('I am sorry but the password does not match')

