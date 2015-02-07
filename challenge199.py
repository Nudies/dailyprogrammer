#Challenge199
#http://www.reddit.com/r/dailyprogrammer/comments/2tr6yn/2015126_challenge_199_bank_number_banners_pt_1/
#You work for a bank, which has recently purchased an ingenious machine
#to assist in reading letters and faxes sent in by branch offices. The
#machine scans the paper documents, and produces a file with a number of
#entries which each look like this:
#    _  _     _  _  _  _  _
#  | _| _||_||_ |_   ||_||_|
#  ||_  _|  | _||_|  ||_| _|
#
#Each entry is 4 lines long, and each line has 27 characters. The first 3
#lines of each entry contain an account number written using pipes and
#underscores, and the fourth line is blank. Each account number should have
#9 digits, all of which should be in the range 0-9.
#Right now you're working in the print shop and you have to take account
#numbers and produce those paper documents.
TOP = {0:' _ ', 1:'   ', 2:' _ ', 3:' _ ', 4:'   ', 5:' _ ', 6:' _ ', 7:' _ ', 8:' _ ', 9:' _ '}
MID = {0:'| |', 1:' | ', 2:' _|', 3:' _|', 4:'|_|', 5:'|_ ', 6:'|_ ', 7:'  |', 8:'|_|', 9:'|_|'}
BOT = {0:'|_|', 1:' | ', 2:'|_ ', 3:' _|', 4:'  |', 5:' _|', 6:'|_|', 7:'  |', 8:'|_|', 9:' _|'}

input = """000000000
111111111
490067715"""

def main(input):
    input = input.strip().split('\n')
    for s in input:
        outTop = ""
        outMid = ""
        outBot = ""
        for i in range(len(s)):
            key = int(s[i])
            outTop += TOP[key]
            outMid += MID[key]
            outBot += BOT[key]
        print outTop
        print outMid
        print outBot
        print ''


if __name__ == '__main__':
    main(input)
