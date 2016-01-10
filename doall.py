#!/usr/bin/env python

import os

for fname in os.listdir('.'):
    if fname.endswith('.png') and not fname.endswith('_.png'):
        os.system('pngtopnm {0} -plain > {1} && ./imageblender.py {1} > {2} && pnmtopng {2} > {3}'.format(fname, fname[:-4]+'.pnm', fname[:-4]+'_.pnm', fname[:-4]+'_.png'))
