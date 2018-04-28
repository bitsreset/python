from flask import Flask , request

app = Flask('__name__')

@app.route('/potato')
def welcome():
    return 'This is my first Flask app!.'

@app.route('/')
def welcome2():
    return 'THIS IS ROOT PAGE'
    
@app.route('/bob')
def welcome3():
    return "Yo Bob what's happening Man!."
 
@app.route( '/method' , methods = [ 'GET' , 'POST' ] )
def method():
    if request.method == "POST":
        return "You've used a POST method."
    else:
        return "You've used a GET method."
    
app.run()