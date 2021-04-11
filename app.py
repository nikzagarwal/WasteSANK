from flask import Flask, render_template , request, url_for 
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import json

with open('templates/config.json','r') as c:
   params = json.load(c)["params"]

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = params['server']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



class Rewarddb(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    company_name=db.Column(db.String(50),nullable=False)
    wasteamt=db.Column(db.Integer,nullable=False)
    wasteamttype=db.Column(db.String(10),nullable=False)
    emailid=db.Column(db.String(50))
    phoneno=db.Column(db.Integer,nullable=False)


class Industrydb(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    plantcap=db.Column(db.Integer,nullable=False)
    waste_collected=db.Column(db.Integer,nullable=False)
    waste_recycled=db.Column(db.Integer,nullable=False)
    Time=db.Column(db.String(20),nullable=False)
    emailid=db.Column(db.String(50),nullable=False)
    phoneno=db.Column(db.Integer)

class Wastedb(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    areaname=db.Column(db.String(30),nullable=False)
    wardno=db.Column(db.Integer,nullable=False)
    drywasteamt=db.Column(db.Integer)
    wetwasteamt=db.Column(db.Integer)
    mixedwasteamt=db.Column(db.Integer)
    
@app.route('/')
def home():        
   return render_template('index.html')

@app.route('/local',methods=['GET','POST'])
def local():        
   urldata="static/waste_gen.csv"
   urldata2="static/recycled_per.csv"
   if request.method=='POST':
      areaname=request.form['area']
      wardno=request.form['ward']
      drywasteamt=request.form['dcollect']
      wetwasteamt=request.form['wcollect']
      mixedwasteamt=request.form['mcollect']
      password=request.form['pass']
      x=Wastedb(areaname=areaname,wardno=wardno,drywasteamt=drywasteamt,wetwasteamt=wetwasteamt,mixedwasteamt=mixedwasteamt)
      if(password==params['p']):
         db.session.add(x)
         db.session.commit()
      return render_template('local.html',urldata=urldata,urldata2=urldata2)
   return render_template('local.html',urldata=urldata,urldata2=urldata2)

@app.route('/reward',methods=['GET','POST'])
def reward():        
   if request.method=='POST':
      name=request.form['name']
      company_name=request.form['comp']
      wasteamt=request.form['collect']
      wasteamttype=request.form['mtype']
      emailid=request.form['email']
      phoneno=request.form['contact']
      x=Rewarddb(name=name, company_name=company_name,wasteamt=wasteamt,wasteamttype=wasteamttype,emailid=emailid,phoneno=phoneno)
      db.session.add(x)
      db.session.commit()
      reward=Rewarddb.query.all()
      return render_template('reward.html',myreward=reward) 
   reward=Rewarddb.query.all()      
   return render_template('reward.html',reward=reward)

@app.route('/locate')
def loacte():        
   return render_template('locate.html')

@app.route('/industry',methods=['GET','POST'])
def industry():       
   if request.method=='POST':
      name=request.form['name']
      plantcap=request.form['plantcap']
      waste_collected=request.form['collect']
      waste_recycled=request.form['recycled']
      Time=request.form['time']
      emailid=request.form['email']
      phoneno=request.form['contact']
      x=Industrydb(name=name, plantcap=plantcap,waste_collected=waste_collected,waste_recycled=waste_recycled,Time=Time,emailid=emailid,phoneno=phoneno)
      db.session.add(x)
      db.session.commit()
      industry=Industrydb.query.all()
      return render_template('industry.html',industry=industry)       
   industry=Industrydb.query.all()
   return render_template('industry.html',industry=industry)

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