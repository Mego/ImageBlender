#!/usr/bin/python

import sys
from itertools import *

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def rgb_to_bin(r,g,b):
    return int(hex(r)[2:] + hex(g)[2:] + hex(b)[2:], 16)

def bin_to_rgb(b):
    h = '%06X'%(b)
    return map(lambda x:int(''.join(x), 16), grouper(h, 2))

def pnm_to_bin(p):
    w,h = map(int,p[1].split(' '))
    data = map(int, ' '.join(p[3:]).replace('\n', ' ').split())
    bin = []
    lines = grouper(data, w*3)
    for line in lines:
        data = []
        for rgb in grouper(line, 3):
            data.append(rgb_to_bin(*rgb))
        bin.append(data)
    return bin

def bin_to_pnm(b):
    pnm = 'P3 {} {} 255 '.format(len(b[0]), len(b))
    b = [z for a in b for z in a]
    pnm += ' '.join(map(lambda x:' '.join(map(str, bin_to_rgb(x))), b))
    return pnm

def imageblender(img):
    h = len(img)
    w = len(img[0])
    for y in range(w):
        for x in range(h):
            val = (img[x][y] + img[x][~y] + img[~x][y] + img[~x][~y])//4
            img[x][y],img[x][~y],img[~x][y],img[~x][~y] = (val,)*4
    return img

def main(fname):
    bin = pnm_to_bin(open(fname).read().split('\n'))
    bin = imageblender(bin)
    return bin_to_pnm(bin)

if __name__ == '__main__':
    print main(sys.argv[1])
