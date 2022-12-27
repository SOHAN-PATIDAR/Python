from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/northwind'
db = SQLAlchemy(app)


class Products(db.Model):
    ProductID = Column(Integer, primary_key=True)        	
    ProductName = Column(String(35))	
    SupplierID = Column(Integer)
    CategoryID = Column(Integer)	
    QuantityPerUnit = Column(String(25))	
    UnitPrice = Column(Numeric(5,2))	
    UnitsInStock = Column(Integer)	
    UnitsOnOrder = Column(Integer)	
    ReorderLevel = Column(Integer)	
    Discontinued = Column(Integer)
    


@app.route("/")
def main():
    return render_template('pro_main.html')


@app.route("/insert",methods=['GET','POST'])
def insert():
    
    if request.method == 'POST':
        "Insert data to database"
        pro_id = request.form['pro_id']
        pro_name = request.form['pro_name']
        sup_id = request.form['sup_id']
        cat_id = request.form['cat_id']
        qpu = request.form['qpu']
        up = request.form['up']
        uis = request.form['uis']
        uoo = request.form['uoo']
        rl = request.form['rl']
        dc = request.form['dc']
        
        
        entry = Products(ProductID= pro_id, ProductName = pro_name,	SupplierID = sup_id,	CategoryID = cat_id,	
                         QuantityPerUnit = qpu,	UnitPrice = up,	UnitsInStock = uis,	UnitsOnOrder = uoo,	ReorderLevel = rl,	Discontinued = dc )
        db.session.add(entry)
        db.session.commit()
        
        return render_template('pro_main.html',var='Data Inserted')
    return render_template('pro_insert.html')

@app.route("/update",methods=['POST','GET'])
def update():
    if request.method == 'POST':
        updt = request.form['updt']
        cond = request.form['cond']
        
        query = f'update products set {updt} where {cond}'
        db.engine.execute(query)
        # for i in r:
        #     print(i)
        return render_template('pro_main.html',var='Record Updated')
    return render_template('pro_update.html')

@app.route("/select",methods=['POST','GET'])
def select():
    if request.method == 'POST':
        column = request.form['column']
        cond = request.form['cond']
        # print(column)
        if cond != '':
            query = f'select {column} from products where {cond}'
        else:
            query = f'select {column} from products'
        r = db.engine.execute(query)
        for i in r:
            print(i)
        return render_template('pro_main.html',var='Data Fetched and can be seen in terminal')
    return render_template('pro_select.html')

app.run(debug=True)