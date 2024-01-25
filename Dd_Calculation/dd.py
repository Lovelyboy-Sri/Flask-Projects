from flask import Flask,request,render_template,url_for,redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def reg():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        num = request.form['cnt']
        p1 = request.form['p1']
        p2 = request.form['p2']

        if p1 == p2:
            user_data['Name'].append(name)
            user_data['Email'].append(email)
            user_data['Contact'].append(num)
            user_data['Password'].append(p1)
            print(name,email,num,p1,p2)
            return redirect(url_for('hello_world',name=name))
        else:
            return redirect(url_for('reg',msg = 'Registration'))
    return render_template('reg.html')

@app.route('/admin')
def admin():
    return user_data

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['p1']
        
        if email in user_data['Email']:
            l = user_data['Email'].index(email)
            if password == user_data['Password'][l]:
                return redirect(url_for('hello_world',name = user_data['Name'][l]))
            else:
                return 'Incorrect Password !'
        else:
            return "Incorrect Email !"
    return render_template('log.html')

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/input',methods=['GET','POST'])
def data():
    return render_template('data.html')

@app.route('/solution',methods=['GET','POST']) 
def ans():
    if request.method == 'POST':
        data1 = int(request.form['Data1'])
        data2 = int(request.form['Data2'])
        
        add = data1 + data2
        sub = data1 - data2
        mul = data1 * data2
        div = data1 / data2

        return render_template('solution.html',add=add,sub=sub,mul=mul,div=div)


if __name__ == '__main__':

    user_data = {
        'Name':[],
        'Email':[],
        'Contact':[],
        'Password':[]
    }

    app.run(debug=True)