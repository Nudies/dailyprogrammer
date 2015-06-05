from random import randint
#One Time Pad

def create_cipher(msg):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    key = []
    out = ''
    for i in msg.lower():
        if i not in alpha:
            out += i
        else:
            shift = randint(0,25)
            key.append(shift)
            out += alpha[(alpha.index(i) + shift) % 26]
    return key, out
        

def unlock_cipher(key, msg):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    count = 0
    for i in msg.lower():
        if i not in alpha:
            out += i
        else:
            out += alpha[(alpha.index(i) - key[count]) % 26]
            count += 1
    return out

