# This is discsweeper
# It takes a single argument, the name of the file you 
# would like to make into a minesweeper.
# 
# See the example for what it should look like. All
# 'b's are turned into bombs and all other characters
# are empty.

import itertools as it
import sys
import os.path as path
from random import randint

emojimap = {
    '*':'💣',
    0:'⬜',
    1:':one:',
    2:':two:',
    3:':three:',
    4:':four:',
    5:':five:',
    6:':six:',
    7:':seven:',
    8:':eight:',
}

filename = sys.argv[1]
print(f'Opening {filename}')

with open(filename, 'r') as bombs:
    bomblist = []
    height,width = 0,0
    for y,line in enumerate(bombs):
        height += 1
        for x,c in enumerate(line):
            if c == 'b':
                bomblist.append((y,x))
    width = x + 1
    field = [[0] * width for _ in range(height)]
    for by,bx in bomblist:
        for dy,dx in it.product([-1,0,1], repeat=2):
            fy,fx = by+dy, bx+dx
            if fy < height and fy >= 0:
                if fx < width and fx >= 0:
                    field[fy][fx] += 1
    
    for by,bx in bomblist:
        field[by][bx] = '*'
    
    maxzero = 0
    for line in field:
        maxzero += sum(1 for c in line if c == 0)
    starter = randint(1,maxzero - 1)


newfilename = '.'.join(filename.split('.')[:-1])
print(f'Writing {newfilename}_disc.txt')
print(f'Writing {newfilename}_plain.txt')
with open(f'{newfilename}_disc.txt', 'w', encoding='utf8') as newfile:
    with open(f'{newfilename}_plain.txt', 'w', encoding='utf8') as plainfile:
        charcount = 0
        for line in field:
            for c in line:
                if c != 0:
                    plainfile.write(str(c) + ' ')
                else:
                    plainfile.write('. ')
                if c == 0:
                    if starter == 0:
                        charcount += newfile.write(emojimap[c])
                    else:
                        charcount += newfile.write(f'||{emojimap[c]}||')
                    starter -= 1
                else:
                    charcount += newfile.write(f'||{emojimap[c]}||')
            plainfile.write('\n')
            newfile.write('\n')

print(f'Message length: {charcount}')
if charcount > 2000:
    print(f'This exceeds discord\'s message length by {charcount - 2000}')