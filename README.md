Transp_Encrypt_Decrypt
======================

A simple program to Encrypt or decrypt English text by transposition

This module will encrypt and decrypt strings using a unique key provide
The encryption and decryption is simple swapping or interchanging of elements
in the string to create Encryption like appearance.

Example:

Encryption
----------
For instance, if we were given the string
               ‘Agent’
			   
Key is [2, 0, 1, 4, 3]

and shuffled it using the above key we would get
               ‘eAgtn’.

Notice that the ‘e’, originally at position 2, now appears first. The ‘A’, originally at
position 0, now appears second. The ‘g’, originally at position 1, now appears third, and so
on.

Decryption
----------
In this case we need the following key to unscramble the original
message.
[1, 2, 0, 4, 3]
Applying this key to rearrange the letters in
                ‘eAgtn’

will again produce
                ‘Agent’

because the ‘A’ in position 1 will be moved to first place, the ‘g’ in position 2 will be moved
to second place, the ‘e’ from position 0 will appear third, etc.
