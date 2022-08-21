from flask import Flask ,request,jsonify
import mysql.connector as conn 

app = Flask(__name__)

@app.route('/insert',methods=["GET","POST"])
def insert():
    if request.method == 'POST':
        mydb = conn.connect(host='localhost',user='root',passwd='R@ud!n$0903',database='FLASQL',use_pure=True)
        cur = mydb.cursor()
        id = request.json['Id']
        name = request.json['Name']
        age = request.json['Age']
        gender = request.json['Gender']
        salary = request.json['SALARY']
        q1 = "INSERT INTO Flask(Id,Name,Age,Gender,SALARY) VALUES (%s,%s,%s,%s,%s)"
        val = (id,name,age,gender,salary)
        cur.execute(q1,val)
        mydb.commit()
        id = cur.lastrowid
        return jsonify((str(id)))

''' {
    "Id": 126,
    "Name": "Gautam",
    "Age": 28,
    "Gender":"Male",
    "SALARY": 87000,
}
''' 

@app.route('/update',methods=["PUT","POST"])
def update():
    if request.method == 'PUT':
        mydb = conn.connect(host='localhost',user='root',passwd='R@ud!n$0903',database='FLASQL',use_pure=True)
        cur = mydb.cursor()
        s1 = request.json['salary']
        n2 = request.json['id']
        query =  "UPDATE Flask SET SALARY = %s WHERE Id = '%s'"
        val1 = (s1,n2)
        cur.execute(query,val1)
        mydb.commit()
        return "Update Successfully"
''' 
{
    "salary": 67000,
    "id":123
}
'''
@app.route('/delete',methods=["DELETE","POST"])
def delete():
    if request.method == 'DELETE':
        mydb = conn.connect(host='localhost',user='root',passwd='R@ud!n$0903',database='FLASQL',use_pure=True)
        cur = mydb.cursor()
        n1 = request.json['id']
        query =  "DELETE FROM Flask WHERE Id ='%s'"%(n1)
        cur.execute(query)
        mydb.commit()
        return 'Delete Successfully'
''' 
{

    "id":127
}

'''

@app.route('/fetch',methods=["GET","POST"])
def fetch():
    if request.method == 'GET':
        mydb = conn.connect(host='localhost',user='root',passwd='R@ud!n$0903',database='FLASQL',use_pure=True)
        cur = mydb.cursor()
        cur.execute("SELECT * FROM Flask")
        result = cur.fetchall()
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)