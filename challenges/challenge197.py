#challenge 197[ez]
#http://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/
#ISBN validater
#Rules:
#Write a function that can return a True i a number is a valid ISBN and False
#othewise.
#Bbtain the sum of 10 times the first digit, 9 times the second digit, 8 times
#the third digit... all the way till you add 1 times the last digit.
#If the sum leaves no remainder when divided by 11 the code is a valid ISBN.
import random

#Check validity of ISBN number
def validate(ISBN):
    if ISBN[-1] == 'X':
        ISBN[-1] = '10'
    for i in range(10):
        ISBN[-(i+1)] = int(ISBN[-(i+1)]) * (i + 1)

    if sum(ISBN) % 11 == 0:
        return True
    else:
        return False


#Generate a vaild ISBN
def generator():
    divCheck = 1
    while divCheck % 11 != 0:
        newISBN = []
        divCheck = 0
        for i in range(10):
            newISBN.append(str(random.randint(0, 9)))
        for i in range(10):
            divCheck += int(newISBN[-(i+1)]) * (i + 1)
    return ''.join(newISBN)


def main():
    ISBN = raw_input('Validate or Generate a ISBN number (\'v\' or \'g\', '
                     '\'q\' to quit)>>> ')

    while ISBN != 'q':
        if ISBN == 'v':
            ISBN = raw_input('Enter a 10 digit number (x-xxxx-xxxx-x or xxxxxxxxxx '
                             '\'q\' to quit)>>> ')

            ISBN = ISBN.replace('-', '')
            if len(ISBN) == 10:
                ISBN = [i for i in ISBN]
                print validate(ISBN)
                break
        elif ISBN == 'g':
            print generator()
            break
        else:
            ISBN = raw_input('Validate or Generate a ISBN number (\'v\' or \'g\', '
                             '\'q\' to quit)>>> ')


if __name__ == '__main__':
    main()
