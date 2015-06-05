#Block Cipher
def create_cipher(key, msg):
    key = [ord(b) for b in key]
    msg = [ord(b) for b in msg]
    out = []

    if len(msg) % len(key) != 0:
        #add padding
        for i in xrange(len(msg) % len(key)):
            key.append(0)

    for x, i in enumerate(msg):
        out.append(format(i ^ key[x % len(key)], 'b'))
    out = ' '.join(out)
    return key, out


def unlock_cipher(key, msg):
    msg = msg.split()
    out = ''
    for x,i in enumerate(msg):
        out += chr(int(i, 2) ^ (key[x % len(key)]))
    return out

