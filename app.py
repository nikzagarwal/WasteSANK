from flask import Flask, render_template , request, url_for 
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from random import randint
import os
import json

with open('templates/config.json','r') as c:
   params = json.load(c)["params"]

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = params['server']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



class Project(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    rawdata=db.Column(db.String(50))
    cleandata=db.Column(db.String(50))
    common=db.Column(db.Integer,nullable=False)




@app.route('/')
def home():        
   return render_template('index.html')

@app.route('/local')
def local():        
   urldata="static/waste_gen.csv"
   urldata2="static/recycled_per.csv"
   return render_template('local.html',urldata=urldata,urldata2=urldata2)

@app.route('/reward')
def reward():        
   return render_template('reward.html')

@app.route('/locate')
def loacte():        
   return render_template('locate.html')

@app.route('/industry')
def industry():       
   return render_template('industry.html')

@app.route('/localform')
def localform():     
      return render_template('localform.html')

@app.route('/rewardform')
def rewardform():        
   return render_template('rewardform.html')

@app.route('/industryform')
def industryform():       
   return render_template('industryform.html')

@app.route('/cluster')
def cluster():       
   return render_template('cluster.html')


if __name__ == '__main__':
   app.run(debug=True)