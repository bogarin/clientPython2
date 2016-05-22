from flask import Flask, render_template, json, request, redirect, session
from Client import Client
#from werkzeug import generate_password_hash, check_password_hash

cliente =Client()
app = Flask(__name__)
app.secret_key = 'por que deveria decir mi clave secreta?'

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route('/showAddWish')
def showAddWish():
    return render_template('addWish.html')

@app.route('/showSignin')
def showSignin():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('signin.html')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Acceso no Autorizado')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if cliente.insertar_usuarios(_name,_email,_password):
        print 'introdujo los datos'
    else:
        print 'no se pudo introducir los datos'



@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    if cliente.verificar_usuario(_username,_password):
        session['user'] = _username
        return redirect('/userHome')
    else:
        return render_template('error.html',error = 'acseso no autorizado')

@app.route('/addWish',methods=['POST'])
def addWish():
    _title = request.form['inputTitle']
    _description = request.form['inputDescription']
    _user = session.get('user')
    if cliente.insertar_comentario(_title,_description,_user):
        return redirect('/userHome')
    else:
        return render_template('error.html',error = 'An error occurred!')

if __name__ == "__main__":
    app.run()
