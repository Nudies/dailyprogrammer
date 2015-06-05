import math
import random
import hashlib

#Don't expect a collision anytime soon!
hash = hashlib.md5()
hash.update('hello')
hash = hash.hexdigest()
print hash

collision = ''
while hash != collision:
    collision = hashlib.md5()
    key = str(math.floor(random.random() * math.pow(2,256))) 
    collision.update(key)
    collision = collision.hexdigest()
else:
    print 'Match Found!\nKey: %s' % key
