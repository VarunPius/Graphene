####################################################################################################
# Library imports
####################################################################################################

# System libraries
import base64

# External libraries
# Argon
from argon2 import hash_password_raw, PasswordHasher

####################################################################################################
# Code start
####################################################################################################


def create_hash(key):
    '''
    Parameters of PasswordHasher() 
    time_cost: int = 3,
    memory_cost: int = 65536,
    parallelism: int = 4,
    hash_len: int = 32,
    salt_len: int = 16,
    encoding: str = 'utf-8',
    type: Type = Type.ID
    '''
    ph = PasswordHasher(hash_len=32,
                        salt_len=16)  # PasswordHasher() can also be used
    hash = ph.hash(key)

    return hash


def process_hash(hash):
    print('Hash: ', hash)

    hash_pwd = hash.split('$')[-1]
    hash_salt = hash.split('$')[-2]
    print('Hashed Pwd: ', hash_pwd)
    print('Hashed salt: ', hash_salt)

    hash_pwd += "=" * ((4 - len(hash_pwd) % 4) % 4)
    hash_salt += "=" * ((4 - len(hash_salt) % 4) % 4)
    hash_pwd_bytes = base64.b64decode(hash_pwd)
    hash_salt_bytes = base64.b64decode(hash_salt)
    print('Hashed Byte Pwd: ', hash_pwd_bytes)
    print('Hashed Byte salt: ', hash_salt_bytes)

    return


def verify(hash, key):
    ph = PasswordHasher()
    try:
        flag = ph.verify(hash, key)
    except Exception as err:
        return err

    return flag


def main():
    passwd1 = "Ampere"
    passwd2 = "Galileo"
    passwd3 = "Tesla"

    hash = create_hash(passwd1)
    process_hash(hash)

    print("Verification 1:", verify(hash, passwd1))
    print("Verification 2:", verify(hash, passwd2))
    print("Verification 3:", verify(hash, passwd3))
    print("Verification 3:", verify(hash, passwd1))


if __name__ == '__main__':
    main()

####################################################################################################
# Notes
####################################################################################################
'''
Output:
Hash:  $argon2id$v=19$m=65536,t=3,p=4$4XVBiJIUlmxY1jlUWPKXKw$qwK9b36xbYnIOlEIsCcIEZpQmMjA4KH5aD1INmcBjxM
Hashed Pwd:  qwK9b36xbYnIOlEIsCcIEZpQmMjA4KH5aD1INmcBjxM
Hashed salt:  4XVBiJIUlmxY1jlUWPKXKw
Hashed Byte Pwd:  b"\xab\x02\xbdo~\xb1m\x89\xc8:Q\x08\xb0'\x08\x11\x9aP\x98\xc8\xc0\xe0\xa1\xf9h=H6g\x01\x8f\x13"
Hashed Byte salt:  b'\xe1uA\x88\x92\x14\x96lX\xd69TX\xf2\x97+'
Verification 1: True
Verification 2: The password does not match the supplied hash
Verification 3: The password does not match the supplied hash
Verification 3: True

Argon2 Notes:
The hash: $argon2id$v=19$m=65536,t=3,p=4$4XVBiJIUlmxY1jlUWPKXKw$qwK9b36xbYnIOlEIsCcIEZpQmMjA4KH5aD1INmcBjxM
The hash is `$` separated.
- The first part `argon2id` specifies the Argon2 algo used, with possible values being argon2i, argon2d and argon2id
- v=19 specifies the version of the algo.
- m=65536 specifies the memory usage
- t=3: computation required or execution time, specified in number of iterations
- p=4: numbe rof parallel threads
- next is the salt,
- the final part is the password hash

The length is 43 characters for hashed password, But it is in base64 format. 
We need to convert it into bytes for it to be used to encrypt using encryption algorithms such as AES

More notes on encoding and salt can be found in the notes 
'''