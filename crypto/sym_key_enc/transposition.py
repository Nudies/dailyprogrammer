#Transposition Cipher
##Columnar Transposition Cipher

def create_cipher(key, msg):
    msg = msg.replace(' ', '').lower()
    out = ['' for i in xrange(key)]
    for x,i in enumerate(msg):
        out[x % key] += i
    return ''.join(out)


def unlock_cipher(key, msg):
    out = ['' for i in xrange(len(msg)/key)]
    for x,i in enumerate(msg):
        out[x % (len(msg) / key)] += i
    return ''.join(out)

