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
