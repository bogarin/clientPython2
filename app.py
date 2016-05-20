from flask import Flask, render_template, json, request
from Client import Client
#from werkzeug import generate_password_hash, check_password_hash

cliente =Client()
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if cliente. insertar_usuarios(_name,_email,_password):
        print 'introdujo los datos'
    else:
        print 'no se pudo introducir los datos'


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

    except Exception as e:
        return render_template('error.html',error = str(e))


if __name__ == "__main__":
    app.run()
