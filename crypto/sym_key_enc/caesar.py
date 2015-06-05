#Caesar Cipher

def create_cipher(key, msg):
    '''
    :type key: int
    :type msg: str
    :rtype: str
    ''' 
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for i in msg.lower():
        if i not in alpha:
            out += i
        else:
            out += alpha[(alpha.index(i) + key) % 26]
    return out


def unlock_cipher(key, msg):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for i in msg.lower():
        if i not in alpha:
            out += i
        else:
            out += alpha[(alpha.index(i) - key) % 26]
    return out

