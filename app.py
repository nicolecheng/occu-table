#!/usr/bin/python

from flask import Flask, render_template
from utils import occu

app = Flask(__name__) #create Flask object


'''
Write a flask app with an "/occupations" route, which will generate an HTML page with an appropriate title, a descriptive heading, and a tablified version of the occupations data. Followed by a randomly selected occupation.
'''

@app.route("/") #assign following fxn to run when root route requested
def homepage():
    d = occu.convertDict("data/occupations.csv")
    oc = occu.picker(d)
    intro1 = "Let me tell you what to do with your life."
    return render_template('occutemp.html', title='Your Future', \
                           intro=intro1, collection=d, \
                           job = oc.lower())

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()



