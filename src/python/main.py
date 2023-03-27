import oracledb
from flask import Flask, render_template, request

user = 'SYSTEM'
password = 'root'
service_name = 'XE'
conn_string = "localhost:{port}/{service_name}".format(
    port=port, service_name=service_name)
app = Flask(__name__)
data = []
id = []

connection = oracledb.connect(
    user=user, password=password, dsn=conn_string)
cur = connection.cursor()
inc_id = cur.execute('select INCIDENT_ID from RPTS.INCIDENTS')
for row in inc_id:
    id.append(row[0])
cur.close()
connection.close()

@app.route('/')
def home():
    return render_template('home.html')