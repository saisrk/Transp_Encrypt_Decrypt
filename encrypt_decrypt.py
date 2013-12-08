"""
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
"""

def append_str(tstr, aval):
    """This method is used by encrypt method to append extra characters
    if needed to match the key length
    @param tstr: This is the string to which character should be appended
    @param aval: This is the count of how much should be appended
    """
    app_var = '_'
    for i in range(aval):
        tstr = tstr + app_var
    
    return tstr

def splitCount(s_str, count):
    """This Method equally divides the appended string into separate
    strings of key length
	@param s_str: This is the string to be split
    @param count: This is the key length into which string must be split
    """
    return [''.join(x) for x in zip(*[list(s_str[z::count]) for z in range(count)])]
 
def traverse_key(s_list, e_key):
    """This Method is responsible for swaping the elements according
    to the encrypt key
    @param s_list: This is the list of strings split from the main string
    @param e_key: This is the key list which tells where tokens must be placed
	"""
    temp_list = []
    for each_str in s_list:
        for each in e_key:
            temp_list.append(each_str[each])
    new_var = ''.join(temp_list)
    return new_var

def encrypt(tar_str, encrypt_key):
    """This Method is used to encrypt the given string using the given key
    @param tar_str: This is the target string to be encrypted
    @param encrypt_key: This is the key for encryption
    """
    str_len = len(tar_str)
    key_len = len(encrypt_key)
    if str_len % key_len != 0:
        app_val = key_len - (str_len % key_len)
        tar_str = append_str(tar_str, app_val)
    str_list = splitCount(tar_str, key_len)
    encrypted_str = traverse_key(str_list, encrypt_key)
    return encrypted_str
    
def decrypt(tar_str, decrypt_key):
    """This Method is used to decrypt the encrypted message given with the key
    @param tar_str: This is the encrypted message
    @param decrypt_key: Key used to decrypt the message
    """
    str_len = len(tar_str)
    key_len = len(decrypt_key)
    if str_len % key_len != 0:
        print "String not properly encrypted. Please input encrypted string"
        pass
    else:
        str_list = splitCount(tar_str, key_len)
        decrypted_str = traverse_key(str_list, decrypt_key).rstrip('_')
    
    return decrypted_str
