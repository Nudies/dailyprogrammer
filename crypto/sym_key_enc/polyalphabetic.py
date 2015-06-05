#Polyalphabetic Cipher aka Vigenere Cipher
'''
Similar to a Caesar Cipher, but instead of shifting by a digit
we shift by the index of a string with len n.
'''

def create_cipher(key, msg):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    key_map = [alpha.index(k) for k in key]
    out = ''
    for x, i in enumerate(msg.lower()):
        if i not in alpha:
            out += i
        else:
            out += alpha[(alpha.index(i) + key_map[x % len(key)]) % 26]
    return out

def unlock_cipher(key, msg):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    key_map = [alpha.index(k) for k in key]
    out = ''
    for x, i in enumerate(msg.lower()):
        if i not in alpha:
            out += i
        else:
            out += alpha[(alpha.index(i) - key_map[x % len(key)]) % 26]
    return out

