from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Verkefni 3</h1><a href="/sidaa">Liður A</a> <a href="/sidab">Liður B</a>'
    
@app.route('/sidaa')
def sidaa():
	return '<h1>Verkefni 3</h1>Alexander Hannesson:</a> <a href="/sida0106982199"> 0106982199</a><br>Karl Óskarsson</a> <a href="/sida1212992345"> 1212992345</a></br>'
    
@app.route('/sida0106982199')
def sida0106982199():
	return '<h1>Þversumma</h1>Þversumma kennitölunnar <b>0106982199</b> er <b>45<b>'
    
@app.route('/sida1212992345')
def sida1212992345():
	return '<h1>Þversumma</h1>Þversumma kennitölunnar <b>1212992345</b> er <b>38<b>'
    
@app.route('/sidab')
def sidab():
	return  render_template("sida0b.html")
    
    
@app.errorhandler(404)
def error404(error):
 return '<h1>Síðan er ekki til!! <br><a href="/"> Smelltu Hér Til Að Komast Aftur Heim</a></h1>', 404
    
       
    

if __name__ == "__main__":
	app.run(debug=True)