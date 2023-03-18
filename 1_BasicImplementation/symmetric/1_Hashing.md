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
