#Challenge196[int]
#http://www.reddit.com/r/dailyprogrammer/comments/2rnwzf/20150107_challenge_196_intermediate_rail_fence/
#Rail fence cipher
#You will accept lines in the format:
#enc # PLAINTEXT
#or
#dec # CIPHERTEXT
#where enc # encodes PLAINTEXT with a rail-fence cipher using # lines, and dec # decodes CIPHERTEXT using # lines.
#For example:
#enc 3 REDDITCOMRDAILYPROGRAMMER
#Output Description
#Encrypt or decrypt depending on the command given. So the example above gives:
#RIMIRAREDTORALPORMEDCDYGM


def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = range(numrails - 1) + range(numrails - 1, 0, -1)
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    return [c for rail in fence for c in rail if c is not None]


def encode(text, n):
    return ''.join(fence(text, n))


def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


def main():
    input = raw_input('[enc|dec] # string >>> ')
    input = input.split()

    if input[0].lower() == 'enc':
            z = encode(input[2], int(input[1]))
            print z
    elif input[0].lower() == 'dec':
            y = decode(input[2], int(input[1]))
            print y


if __name__ == '__main__':
    main()
