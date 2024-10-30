Caesar Cipher is a classical cryptographic technique used for encoding text by shifting each letter a certain number of places down or up the alphabet, according to a specified key. 
This results in an unreadable cipher text. The same key is used to decrypt the cipher text back to its original form by reversing the shift.

How the Caesar Cipher Works
The Caesar Cipher operates by taking each character in a message and shifting it forward (for encryption) or backward (for decryption) through the alphabet by a fixed number of positions specified by a "key." 
For example, with a key of `3`:
- `A` becomes `D`
- `B` becomes `E`
- `Z` wraps around to become `C`

Example
Given the word "HELLO" and a key of `3`:
- Encrypted text: `KHOOR`
- Decrypted back: `HELLO`

Installation
This script requires no additional libraries. Clone this repository and run the script in any Python environment.

```bash
git clone https://github.com/yourusername/caesar-cipher.git
cd caesar-cipher
