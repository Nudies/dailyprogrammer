#challenge 198[easy]
#http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/

#challenge inputs

wordInput = 'because cause'
# hello below
# hit miss
# rekt pwn
# combo jumbo
# critical optical
# isoenzyme apoenzyme
# tribesman brainstem
# blames nimble
# yakuza wizard
# longbow blowup

#No using sets!
def words(leftWord, rightWord):
    for i in leftWord + rightWord:
        if i in leftWord and i in rightWord:
            leftWord = leftWord.replace(i, '', 1)
            rightWord =rightWord.replace(i, '', 1)
    if len(leftWord) == len(rightWord):
        print 'Tie!'
    elif len(leftWord) > len(rightWord):
        print 'Left side wins!'
    else:
        print 'Right side wins!'
    return


def main(wordInput):
    leftright = wordInput.split()
    words(leftright[0], leftright[1])
    return


if __name__ == '__main__':
    main(wordInput)
