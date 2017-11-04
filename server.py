from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
   print request.form
   name1 = request.form['name']
   location1 = request.form['location']
   print location1
   Language1= request.form['Language']
   comments1 = request.form['Comments']
   return render_template('/results.html', name=name1, Location=location1, Language=Language1, Comments=comments1)


@app.route('/results/<survey>', methods=['GET'])
def survey(survey):
    print "Tag you are it."
    return render_template ('/results.html',survey = survey)

def button():
    print "you asked to be redirected"
    return render_template('/')

app.run(debug=True) 