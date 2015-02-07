#Challenge 200[intermed] Metro tile meltdown
#http://www.reddit.com/r/dailyprogrammer/comments/2uo3yf/20150204_challenge_200_intermediate_metro_tile/ 
"""In the name of backward-compatibility, Microsoft has released
a version of their flagship operating system for VGA text-mode terminals.
 In this version of their operating system, rectangular tiles consisting
of a single character are displayed on the screen, like so:"""
input = """..........................................................................
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
................................bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
...................cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.............................jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee...............................................................
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.........................................................................."""
"""Screen space with no tile is denoted by a period (.). Tiles can be made of
any character other than periods (due to the reason given) and spaces.
However, the dev team forgot to add support for screen-readers! Now visually
impaired users cannot determine the location of the tiles on their display.
Your task is, given a tile display such as the one above, write a program to
find the location and size of each rectangular tile on the screen, along with
the character in it, and output it in a way that can be read by a screen
reader. For example, one such tile in the above example is located at position
(1, 1) on the screen (from the top-left), consists of the character a and
is 30 characters wide and 8 characters tall."""

def makeWorld(map):
    """Turn the string input into a 2d matrix"""
    map = map.strip().split('\n')
    world = [[] for i in map]
    for i in range(len(map)):
        for x in map[i]:
            world[i].append(x)

    return parseWorld(world, 74, 30)


def parseWorld(world, w, h, x=0, y=0):
    """Store values that are not spaces (.) in a dict.
    The dict holds the x, y cord for each occurence of
    the key.
    ex: {a: [(x,y), (x+1,y+1)]}"""
    worldMap = {}
    while x != w - 1 or y != h - 1:
        if world[y][x] != '.' and world[y][x] not in worldMap.keys():
            worldMap[world[y][x]] = []
        if world[y][x] in worldMap.keys():
            worldMap[world[y][x]].append((x ,y))
        if x < w - 1:
            x += 1
        elif y < h - 1 and x == w-1:
            x = 0
            y += 1
    return worldMap


def main(input):
    map = makeWorld(input)
    for k in map.keys():
        dimensionX =  map[k][-1][0] - map[k][0][0] + 1
        dimensionY = map[k][-1][1] - map[k][0][1] + 1
        startCords = map[k][0]
        print '%sx%s tile of character \'%s\' located at %s' % (dimensionX,
                dimensionY, k, startCords)


if __name__ == '__main__':
    main(input)
