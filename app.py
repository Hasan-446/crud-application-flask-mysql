from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app= Flask(__name__)
app.secret_key="flaskcrud"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskcrud'

mysql=MySQL(app)

@app.route("/")
def index():

    cur =mysql.connection.cursor()
    cur.execute("select * from student")
    data=cur.fetchall()
    cur.close()
    return render_template ("index.html", students=data)

@app.route("/insert", methods=['POST'])
def insert():
     

    if request.method == "POST" :

        studentId= request.form['studentId']
        email= request.form['email']
        name= request.form['name']
        dept= request.form['dept']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `student`( `id`, `name`, `email`, `dept`) VALUES (%s,%s,%s,%s)", (studentId, name, email,dept) )
        mysql.connection.commit()
        flash("data inserted success",'success')
        return redirect (url_for('index'))

@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method=='POST':
        serial_data=request.form['serial']
        studentId= request.form['studentId']
        email= request.form['email']
        name= request.form['name']
        dept= request.form['dept']

        cur = mysql.connection.cursor()
        cur.execute(" UPDATE `student` set id =%s ,name= %s ,email=%s ,dept=%s where serial=%s ",(studentId, name, email,dept,serial_data))
        mysql.connection.commit()
        flash("data updated success",'success')
        return redirect (url_for('index'))

@app.route("/delete/<string:serial> ", methods=['GET'])
def delete(serial):
    cur = mysql.connection.cursor()
    cur.execute(" DELETE FROM `student` WHERE serial=%s ",(serial,))
    mysql.connection.commit()
    flash("data delete",'success')
    return redirect (url_for('index'))
    
    
if __name__=='__main__':
    app.run(debug=True)
    