# Graphene
This repo is focused on Cryptography and cyber security learnings.


# Cryptography
Cryptography is the study of taking in data and scrambling it so that it ensures security and privacy of the users. In simple words, it's the science of creating secrets.

The main topics in Basics of Cryptography are:
- Hashing
- Salting
- Encoding
- Encryption
    - Symmetrical
    - Asymmetrical


# Hashing
Hashing is the process of transforming any given key or a string of characters into another value.
It has culinary roots from the concept of chopping and mixing (hence hashing as in hash potatoes)

The most popular use for hashing is the implementation of hash tables.
A hash table stores key and value pairs in a list that is accessible through its index.
Because key and value pairs are unlimited, the hash function will map the keys to the table size.
A hash value then becomes the index for a specific element.

A hash function generates new values according to a mathematical hashing algorithm, known as a hash value or simply a hash.
To prevent the conversion of hash back into the original key, a good hash always uses a one-way hashing algorithm.

In cryptography, a special has function called *key derivation function* (KDF) is used. KDF is a cryptographic algorithm that derives one or more secret keys from a secret value such as a master key, a password, or a passphrase using a pseudorandom function (which typically uses a cryptographic hash function or block cipher).
KDFs can be used to stretch keys into longer keys or to obtain keys of a required format, such as converting a group element that is the result of a *Diffie–Hellman key exchange* into a symmetric key for use with AES. 

Hashing is relevant to -- but not limited to -- data indexing and retrieval, digital signatures, cybersecurity and cryptography.

The key point of an hashing algorithm is given same input, it will always yield same output. Another thing to note is, in cryptography use case, it is extremely difficult to get the original password back from the hashed key (i.e input will yield same output but given an output, you can't know the input)

Examples of Hash function:
- **MD5**:
    - Digest Size: 128 bit
    Deprecated as can be easily hacked
- **SHA**:
    - Digest Size: 256 bit for SHA-256, 512 bits for SHA-512
- **Argon2**:
    Currently the best Key derivation function
    - Digest size: upto 2^32 bytes long
    Has 3 different modes:
        - *Argon2d* maximizes resistance to GPU cracking attacks. It accesses the memory array in a password dependent order, which reduces the possibility of time–memory trade-off (TMTO) attacks, but introduces possible side-channel attacks.
        - *Argon2i* is optimized to resist side-channel attacks. It accesses the memory array in a password independent order.
        - *Argon2id* is a hybrid version. It follows the Argon2i approach for the first half pass over memory and the Argon2d approach for subsequent passes. The RFC recommends using Argon2id if you do not know the difference between the types or you consider side-channel attacks to be a viable threat.
- **bcrypt**:
    - Digest Size: 184 bit
    Derived from Blowfish(cipher)
- **scrypt**:
    Proof of concept used in crypto mining


# Salting
The fact that hashing function returns the same value is a problem. This is because a hacker can build a rainbow table of all possible passwords and the corresponding hashed value and looking at the hash value from the table, he can reverse engineer the original password.

Salt is a random value added to the password before hashing.

> Note: The salt used during hash creation needs to be saved as during verification, this salt and the password will be used to compare against the hashed value. Remember, salt is a random value added to password during hash creation and thus any further comparison/verification against this hash needs to have the original salt.

Common way of saving salt is `salt:hashedPassword`. Another way as done by `Argon2` is `$salt$hashedPassword`

# Encoding
To store the human-readable characters on computers, we need to **encode** them into bytes.
In contrast, we need to decode the bytes into human-readable characters for representation.

Byte, in computer science, indicates a unit of `0/1`, commonly of length 8. So characters `Hi` are actually stored as `01001000 01101001` on the computer, which consumes 2 bytes (16-bits).

The rule that defines the encoding process is called **encoding schema**. Commonly used ones include *ASCII*, *UTF-8* and *UTF-16*. 

Now, the question how do these encoding schemas look like?

**ASCII** converts each character into one byte. Since one byte consisted of 8 bits and each bit contains 0/1. The total number of characters ASCII can represent is `2^8 = 256`. It is more than enough for 26 English letters plus some commonly-used characters such as `$`.

However, 256 characters are obviously not enough for storing all the characters in the world. 
In light of that, people designed Unicode in which each character will be encoded as a **code point**. 
For instance, `H` will be represented as code point `U+0048`.

According to Wikipedia, Unicode can include 144,697 characters.
But again, the code point still can not be recognized by the computer, so we have UTF-8 or other variants encoding schema to convert the code point to the byte.

**UTF-8** means the minimum length of bits to represent a character is 8, so you can guess, **UTF-16** means the minimum length of bits is 16. 

With the basic concepts understood, let’s cover some practical coding tips in Python. 

In Python3, the default string is called Unicode string (`u` string), you can understand them as human-readable characters. As explained above, you can encode them to the byte string (`b` string), and the byte string can be decoded back to the Unicode string.

```py
u'Hi'.encode('ASCII')
> b'Hi'
b'\x48\x69'.decode('ASCII')
> 'Hi'
```
In Python IDE, usually, the byte string will be automatically decoded using ASCII when printed out, so that’s why the first result is human-readable (`b'Hi'`). More often, Byte string should be represented as Hex code (`b'\x48\x69'`).

This is important to remember, because when we hash our passwords and print it, some algorithms such as Argon2 will display base64 data. That is, even if 32-byte (256 bit) binary hash is generated, this will be encoded into base64 and displayed as a 43 character long string. Now, in base64, everything is encoded into 64 characters (A-Z, a-z, 0-9, +, /). This would 2^6 chanarcters. So, 6-bits can be used to display characters. As a result, the 256 bits will yield 43 characters. As a result, we would need to decode this base64 characters to convert them into binary bytes.
Check {$ref(hashcode)} for code example

## Base64 Padding
Padding characters help satisfy length requirements and carry no other meaning.

Decimal Example of Padding: Given the arbitrary requirement all strings be 8 characters in length, the number 640 can meet this requirement using preceding 0's as padding characters as they carry no meaning, `00000640`.

The Byte Paradigm: For encoding, the byte is the de facto standard unit of measurement and any scheme must relate back to bytes.
- **Base256** fits exactly into the byte paradigm. One byte is equal to one character in base256.
- **Base16** hexadecimal or hex, uses 4 bits for each character. One byte can represent two base16 characters.
- **Base64** does not fit evenly into the byte paradigm (nor does `base32`), unlike base256 and base16. All base64 characters can be represented in 6 bits, 2 bits short of a full byte.

We can represent base64 encoding versus the byte paradigm as a fraction: 6 bits per character over 8 bits per byte.
Reduced this fraction is 3 bytes over 4 characters.

This ratio, 3 bytes for every 4 base64 characters, is the rule we want to follow when encoding base64.
Base64 encoding can only promise even measuring with 3 byte bundles, unlike base16 and base256 where every byte can stand on it's own.

So why is padding encouraged even though encoding could work just fine without the padding characters?

If the length of a stream is unknown or if it could be helpful to know exactly when a data stream ends, use padding.
The padding characters communicate explicitly that those extra spots should be empty and rules out any ambiguity.
Even if the length is unknown with padding you'll know where your data stream ends.

Suppose we have a program that base64-encodes words, concatenates them and sends them over a network. It encodes "I", "AM" and "TJM", sandwiches the results together without padding and transmits them.
- I encodes to SQ (SQ== with padding)
- AM encodes to QU0 (QU0= with padding)
- TJM encodes to VEpN (VEpN with padding)

So the transmitted data is SQQU0VEpN. The receiver base64-decodes this as I\x04\x14\xd1Q) instead of the intended IAMTJM. The result is nonsense because the sender has destroyed information about where each word ends in the encoded sequence. If the sender had sent SQ==QU0=VEpN instead, the receiver could have decoded this as three separate base64 sequences which would concatenate to give IAMTJM.

This is important to remember because decoding from base64 to bytes may sometimes result in an error depending on the protocol/library used so ensure base64 hash has padding before we start decoding.

## TLDR:
- UTF-8 and UTF-16 are methods to encode Unicode strings to byte sequences.
- Base64 is a method to encode a byte sequence to a string.

Things to keep in mind:
- Not every byte sequence represents an Unicode string encoded in UTF-8 or UTF-16.
- Not every Unicode string represents a byte sequence encoded in Base64.

---
# Appendix

## Argon2:
https://argon2-cffi.readthedocs.io/en/latest/
https://medium.com/@ashiqgiga07/cryptography-with-python-hashing-d0b7dbf7767
https://medium.com/analytics-vidhya/password-hashing-pbkdf2-scrypt-bcrypt-and-argon2-e25aaf41598e
https://www.alexedwards.net/blog/how-to-hash-and-verify-passwords-with-argon2-in-go

# Appendix
- AES
https://onboardbase.com/blog/aes-encryption-decryption/
https://hackernoon.com/how-to-use-aes-256-cipher-python-cryptography-examples-6tbh37cr

- Libsodium
https://developer.okta.com/blog/2021/08/05/libsodium-encryption-go-python

- Fernet
https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
https://www.alixaprodev.com/2022/05/encrypt-files-and-directories-in-python.html

https://askubuntu.com/questions/98443/encrypting-files-and-folder-through-terminal
https://en.wikipedia.org/wiki/Cryptographic_hash_function



