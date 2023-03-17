# Graphene
Cryptography learnings

# Cryptography
Cryptography is the study of taking in data and scrambling it so that it ensures security and privacy of the users. In simple words, it's the science of creating secrets.

The main topics in Basics of Cryptography are:
- Hashing

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

## Encoding

---
# Notes
# Encoding
- base64


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



# Encoding:
## Padding
However, padding is useful in situations where base64 encoded strings are concatenated in such a way that the lengths of the individual sequences are lost, as might happen, for example, in a very simple network protocol.

If unpadded strings are concatenated, it's impossible to recover the original data because information about the number of odd bytes at the end of each individual sequence is lost. However, if padded sequences are used, there's no ambiguity, and the sequence as a whole can be decoded correctly.
Edit: An Illustration

Suppose we have a program that base64-encodes words, concatenates them and sends them over a network. It encodes "I", "AM" and "TJM", sandwiches the results together without padding and transmits them.

    I encodes to SQ (SQ== with padding)
    AM encodes to QU0 (QU0= with padding)
    TJM encodes to VEpN (VEpN with padding)

So the transmitted data is SQQU0VEpN. The receiver base64-decodes this as I\x04\x14\xd1Q) instead of the intended IAMTJM. The result is nonsense because the sender has destroyed information about where each word ends in the encoded sequence. If the sender had sent SQ==QU0=VEpN instead, the receiver could have decoded this as three separate base64 sequences which would concatenate to give IAMTJM.
Why Bother with Padding?

Why not just design the protocol to prefix each word with an integer length? Then the receiver could decode the stream correctly and there would be no need for padding.

That's a great idea, as long as we know the length of the data we're encoding before we start encoding it. But what if, instead of words, we were encoding chunks of video from a live camera? We might not know the length of each chunk in advance.

If the protocol used padding, there would be no need to transmit a length at all. The data could be encoded as it came in from the camera, each chunk terminated with padding, and the receiver would be able to decode the stream correctly.

Obviously that's a very contrived example, but perhaps it illustrates why padding might conceivably be helpful in some situations.

## second solution:
https://stackoverflow.com/questions/4080988/why-does-base64-encoding-require-padding-if-the-input-length-is-not-divisible-by
What are Padding Characters?

Padding characters help satisfy length requirements and carry no other meaning.

Decimal Example of Padding: Given the arbitrary requirement all strings be 8 characters in length, the number 640 can meet this requirement using preceding 0's as padding characters as they carry no meaning, "00000640".
Binary Encoding

The Byte Paradigm: For encoding, the byte is the de facto standard unit of measurement and any scheme must relate back to bytes.

Base256 fits exactly into the byte paradigm. One byte is equal to one character in base256.

Base16, hexadecimal or hex, uses 4 bits for each character. One byte can represent two base16 characters.

Base64 does not fit evenly into the byte paradigm (nor does base32), unlike base256 and base16. All base64 characters can be represented in 6 bits, 2 bits short of a full byte.

We can represent base64 encoding versus the byte paradigm as a fraction: 6 bits per character over 8 bits per byte. Reduced this fraction is 3 bytes over 4 characters.

This ratio, 3 bytes for every 4 base64 characters, is the rule we want to follow when encoding base64. Base64 encoding can only promise even measuring with 3 byte bundles, unlike base16 and base256 where every byte can stand on it's own.

So why is padding encouraged even though encoding could work just fine without the padding characters?

If the length of a stream is unknown or if it could be helpful to know exactly when a data stream ends, use padding. The padding characters communicate explicitly that those extra spots should be empty and rules out any ambiguity. Even if the length is unknown with padding you'll know where your data stream ends.

As a counter example, some standards like JOSE don't allow padding characters. In this case, if there is something missing, a cryptographic signature won't work or other non base64 characters will be missing (like the "."). Although assumptions about length aren't made, padding isn't needed because if there is something wrong it simply won't work.

And this is exactly what the base64 RFC says,

    In some circumstances, the use of padding ("=") in base-encoded data is not required or used. In the general case, when assumptions about the size of transported data cannot be made, padding is required to yield correct decoded data.

    [...]

    The padding step in base 64 [...] if improperly implemented, lead to non-significant alterations of the encoded data. For example, if the input is only one octet for a base 64 encoding, then all six bits of the first symbol are used, but only the first two bits of the next symbol are used. These pad bits MUST be set to zero by conforming encoders, which is described in the descriptions on padding below. If this property do not hold, there is no canonical representation of base-encoded data, and multiple base- encoded strings can be decoded to the same binary data. If this property (and others discussed in this document) holds, a canonical encoding is guaranteed.

Padding allows us to decode base64 encoding with the promise of no lost bits. Without padding there is no longer the explicit acknowledgement of measuring in three byte bundles. Without padding you may not be able to guarantee exact reproduction of original encoding without additional information usually from somewhere else in your stack, like TCP, checksums, or other methods.

Alternatively to bucket conversion schemes like base64 is radix conversion which has no arbitrary bucket sizes and for left-to-right readers is left padded. The "iterative divide by radix" conversion method is typically employed for radix conversions.
Examples

Here is the example form RFC 4648 (https://www.rfc-editor.org/rfc/rfc4648#section-8)

Each character inside the "BASE64" function uses one byte (base256). We then translate that to base64.

BASE64("")       = ""           (No bytes used. 0 % 3 = 0)
BASE64("f")      = "Zg=="       (One byte used. 1 % 3 = 1)
BASE64("fo")     = "Zm8="       (Two bytes.     2 % 3 = 2)
BASE64("foo")    = "Zm9v"       (Three bytes.   3 % 3 = 0)
BASE64("foob")   = "Zm9vYg=="   (Four bytes.    4 % 3 = 1)
BASE64("fooba")  = "Zm9vYmE="   (Five bytes.    5 % 3 = 2)
BASE64("foobar") = "Zm9vYmFy"   (Six bytes.     6 % 3 = 0)

## utf8 base64:
UTF-8 and UTF-16 are methods to encode Unicode strings to byte sequences.
Base64 is a method to encode a byte sequence to a string.

Things to keep in mind:
- Not every byte sequence represents an Unicode string encoded in UTF-8 or UTF-16.
- Not every Unicode string represents a byte sequence encoded in Base64.

## 43 byte length output
The hasher generates a 32-byte output. It looks like you, at some point you or the library have used Base64 encoding which does a 4-to-3 expansion of the bytes to convert it into printable characters. To get the 32-bytes expected by AES, you'll need to unencode. 