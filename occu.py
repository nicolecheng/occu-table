#!/usr/bin/python

import random

from flask import Flask, render_template
app = Flask(__name__) #create Flask object


'''
Write a flask app with an "/occupations" route, which will generate an HTML page with an appropriate title, a descriptive heading, and a tablified version of the occupations data. Followed by a randomly selected occupation.
'''

@app.route("/") #assign following fxn to run when root route requested
def homepage():
    return render_template('occutemp.html', title='Your Future', \
                           intro=intro1, collection=dict2(), \
                           job = occupations())

intro1 = "Let me tell you what to do with your life."

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

def dict2():
    return convertDict('occupations.csv')

def picker(dict):
    percentage = random.random() * 99.8
    counter = 0
    for item in dict:
        if percentage > dict[item] + counter:
            counter += dict[item]
        else:
            return item
        
def occupations():
    dict = convertDict("occupations.csv")
    return picker(dict).lower()

    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

#return occupations()
