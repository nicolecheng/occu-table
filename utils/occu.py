#!/usr/bin/python

# occupaciones

import random

def convertDict(x):
    d = {}
    f = open(x)
    f.readline()
    m = f.readline()
    while m!='':
        if m[0]=='"':
            m = m[1:]
            n = m.index('"')+1 # finds index of second "
            d[m[:n-1]] = float(m[n+1:])
        else:
            n = m.index(',')
            if(m[0:5]!='Total'):
                d[m[:n]] = float(m[n+1:]) # add the kv pair to d
        m = f.readline() # next line, por favor
    return d

def picker(dict):
    percentage = random.random() * 99.8
    counter = 0
    for item in dict:
        if percentage > dict[item] + counter:
            counter += dict[item]
        else:
            return item

