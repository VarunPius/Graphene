'''
Step 1 in any encryption is hashing the password to generate a key.

When you enter a password, the hashing algorithm generates a key. 

'''

from argon2 import PasswordHasher


def create_hash(key):
    ph = PasswordHasher()
    hash = ph.hash(key)

    return hash


def verify(hash, key):
    ph = PasswordHasher()
    try:
        flag = ph.verify(hash, key)
    except Exception as err:
        return err

    return flag


def main():
    key1 = "Ampere"
    key2 = "Galileo"
    key3 = "Tesla"

    hash = create_hash(key1)

    print("Verification 1:", verify(hash, key1))
    print("Verification 2:", verify(hash, key2))
    print("Verification 3:", verify(hash, key3))
    print("Verification 3:", verify(hash, key1))


if __name__ == '__main__':
    main()