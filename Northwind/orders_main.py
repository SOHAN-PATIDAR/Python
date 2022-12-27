from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/northwind'
db = SQLAlchemy(app)


class Orders(db.Model):
    ProductID = Column(Integer, primary_key=True)        	
    
    OrderID = Column(Integer,primary_key=True)
    CustomerID = Column(String(25))	
    EmployeeID = Column(Integer)	
    OrderDate = Column(String(25))	
    RequiredDate = Column(String(25))	
    ShippedDate = Column(String(25))	
    ShipVia = Column(Integer)	
    Freight = Column(Numeric(6,2))	
    ShipName = Column(String(35))	
    ShipAddress = Column(String(50))	
    ShipCity = Column(String(25))	
    ShipRegion = Column(String(25))	
    ShipPostalCode = Column(String(25))	
    ShipCountry = Column(String(25))
    


@app.route("/")
def main():
    return render_template('ord_main.html')


@app.route("/insert",methods=['GET','POST'])
def insert():
    
    if request.method == 'POST':
        "Insert data to database"
        ord_id = request.form['ord_id']
        cus_id = request.form['cus_id']
        emp_id = request.form['emp_id']
        ord_date = request.form['ord_date']
        rq_date = request.form['rq_date']
        shp_date = request.form['shp_date']
        sv = request.form['sv']
        fr = request.form['fr']
        shp_name = request.form['shp_name']
        shp_adr = request.form['shp_adr']
        shp_city = request.form['shp_city']
        shp_rgn = request.form['shp_rgn']
        shp_pin = request.form['shp_pin']
        shp_ctr = request.form['shp_ctr']
        
        
        entry = Orders(OrderID = ord_id,CustomerID =cus_id ,	EmployeeID =emp_id ,	OrderDate =ord_date ,	RequiredDate =rq_date ,	ShippedDate = shp_date,	
                       ShipVia = sv,	Freight = fr,	ShipName = shp_name,	ShipAddress = shp_adr,	ShipCity =shp_city ,	
                       ShipRegion = shp_rgn,	ShipPostalCode =shp_pin ,	ShipCountry =shp_ctr ,)
        db.session.add(entry)
        db.session.commit()
        
        return render_template('ord_main.html',var='Data Inserted')
    return render_template('ord_insert.html')

@app.route("/update",methods=['POST','GET'])
def update():
    if request.method == 'POST':
        updt = request.form['updt']
        cond = request.form['cond']
        
        query = f'update orders set {updt} where {cond}'
        db.engine.execute(query)
        # for i in r:
        #     print(i)
        return render_template('ord_main.html',var='Record Updated')
    return render_template('ord_update.html')

@app.route("/select",methods=['POST','GET'])
def select():
    if request.method == 'POST':
        column = request.form['column']
        cond = request.form['cond']
        # print(column)
        if cond != '':
            query = f'select {column} from orders where {cond}'
        else:
            query = f'select {column} from orders'
        r = db.engine.execute(query)
        for i in r:
            print(i)
        return render_template('ord_main.html',var='Data Fetched and can be seen in terminal')
    return render_template('ord_select.html')

app.run(debug=True)