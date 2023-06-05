
# ToDo:
## Use a Secure Hash Meant for Passwords
https://www.howtogeek.com/devops/how-to-properly-store-passwords-salting-hashing-and-pbkdf2/
While SHA256 is a secure hash, it’s also designed to be a general-purpose hash. This means it has to be fast, because it’s also used for creating checksums (which must process gigabytes of data). Speed directly decreases bruteforcing time, and even with salted passwords, it’s still relatively easy to crack individual short strings. Salts only protect against rainbow tables.

Instead, use PBKDF2. It’s meant specifically for passwords, meaning it’s relatively slow to calculate for the average length password. It takes much longer to bruteforce, and it’s practically impossible to crack longer passwords stored with it. You can use the JavaScript implementation, or use a server side implementation.

To make full use of PBKDF2, you’ll want to implement some sort of password standard for your site. You don’t need to require everyone to have dollar signs and numbers in there; length matters much more than anything else. Try to enforce 8-12 character passwords at a minimum.