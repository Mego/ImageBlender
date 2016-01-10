#!/usr/bin/python

import sys
from itertools import *

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return list(izip_longest(*args, fillvalue=fillvalue))

def flatten(lst):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])

def pnm_to_bin(p):
    w,h = map(int,p[1].split(' '))
    data = map(int, ' '.join(p[3:]).replace('\n', ' ').split())
    bin = []
    lines = grouper(data, w*3)
    for line in lines:
        data = []
        for rgb in grouper(line, 3):
            data.append(list(rgb))
        bin.append(data)
    return bin

def bin_to_pnm(b):
    pnm = 'P3 {} {} 255 '.format(len(b[0]), len(b))
    b = flatten(b)
    pnm += ' '.join(map(str, b))
    return pnm

def imageblender(img):
    h = len(img)
    w = len(img[0])
    for y in range(w):
        for x in range(h):
            for i in range(3):
                val = (img[x][y][i] + img[x][~y][i] + img[~x][y][i] + img[~x][~y][i])//4
                img[x][y][i],img[x][~y][i],img[~x][y][i],img[~x][~y][i] = (val,)*4
    return img

def main(fname):
    bin = pnm_to_bin(open(fname).read().split('\n'))
    bin = imageblender(bin)
    return bin_to_pnm(bin)

if __name__ == '__main__':
    print main(sys.argv[1])
