from flask import Flask, render_template,request
import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hdj19914;PWD=hwFw5qwF1TR6TWLc;","","")

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
  return render_template("Home.html")

@app.route("/SignUp",methods=['GET', 'POST'])
def SignUp():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        print(name,email,password)
        insert_sql = "INSERT INTO HDJ19914.PERSONS VALUES (?, ?, ?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, password)
        ibm_db.bind_param(prep_stmt, 3, email)
        ibm_db.execute(prep_stmt)
        return render_template('login.html', msg = msg) 
    else:
        return render_template('SignUp.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])

def login():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        select_sql = "SELECT * FROM HDJ19914.PERSONS WHERE USERNAME = ? AND PASSWORD = ?"
        prep_stmt = ibm_db.prepare(conn, select_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, password)
        out = ibm_db.execute(prep_stmt)
        result_dict = ibm_db.fetch_assoc(prep_stmt)
        print(result_dict)
        if result_dict != False:
            return render_template('Home.html',msg = msg)
        return render_template('login.html', msg = msg)

    else:
        return render_template('login.html', msg = msg)


@app.route("/about")
def about():
  return render_template("About.html")

@app.route("/login")
def signin():
  return render_template("login.html")

@app.route("/signup")
def signup():
  return render_template("SignUp.html")

@app.route("/forgot")
def forgot():
  return render_template("forgot.html")