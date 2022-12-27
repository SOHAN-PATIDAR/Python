from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/northwind'
db = SQLAlchemy(app)


@app.route("/",methods=['GET','POST'])
def main():
    if request.method == "POST":
        cus_id = request.form['cus_id']

        query = f"select * from orders where CustomerID = '{cus_id}'"
        r = db.engine.execute(query)
        for i in r:
            print(f"OrderID: {i[0]},  EmployeeID: {i[2]},  OrderDate: {i[3]},  RequiredDate: {i[4]},  ShippedDate: {i[5]},  ShipVia: {i[6]},  Freight: {i[7]},  ShipName: {i[8]},  ShipAddress: {i[9]},  ShipCity: {i[10]},  ShipRegion: {i[11]},  ShipPostalCode: {i[12]},  ShipCountry: {i[13]}",end="\n\n")
            
    return render_template('ord_his_main.html')

app.run(debug=True)