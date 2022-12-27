from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/northwind'
db = SQLAlchemy(app)


class Customers(db.Model):
    
    CustomerID = db.Column(db.String(80))
    CompanyName = db.Column(db.String(80))
    ContactName = db.Column(db.String(80))	
    ContactTitle = db.Column(db.String(80))	
    Address = db.Column(db.String(80))	
    City = db.Column(db.String(80))	
    Region = db.Column(db.String(80))	
    PostalCode = db.Column(db.String(80))	
    Country = db.Column(db.String(80))	
    Phone = db.Column(db.String(80),primary_key=True)	
    Fax = db.Column(db.String(80))
    


@app.route("/")
def main():
    return render_template('cus_main.html')


@app.route("/insert",methods=['GET','POST'])
def insert():
    
    if request.method == 'POST':
        "Insert data to database"
        cid = request.form['cus_id']
        cname = request.form['com_name']
        ctname = request.form['con_name']
        cttitle = request.form['con_title']
        adr = request.form['adr']
        city = request.form['city']
        rgn = request.form['region']
        pin = request.form['pin']
        cntr = request.form['country']
        phone = request.form['phone']
        fax = request.form['fax']
        
        entry = Customers(CustomerID=cid, CompanyName=cname,ContactName=ctname,ContactTitle=cttitle,Address=adr,
                          City=city,Region=rgn,PostalCode=pin,Country=cntr,Phone=phone,Fax=fax)
        db.session.add(entry)
        db.session.commit()
        
        return render_template('cus_main.html',var='Data Inserted')
    return render_template('cus_insert.html')

@app.route("/update",methods=['POST','GET'])
def update():
    if request.method == 'POST':
        updt = request.form['updt']
        cond = request.form['cond']
        
        query = f'update customers set {updt} where {cond}'
        db.engine.execute(query)
        # for i in r:
        #     print(i)
        return render_template('cus_main.html',var='Record Updated')
    return render_template('cus_update.html')

@app.route("/select",methods=['POST','GET'])
def select():
    if request.method == 'POST':
        column = request.form['column']
        cond = request.form['cond']
        # print(column)
        if cond != '':
            query = f'select {column} from customers where {cond}'
        else:
            query = f'select {column} from customers'
        r = db.engine.execute(query)
        for i in r:
            print(i)
        return render_template('cus_main.html',var='Data Fetched and can be seen in terminal')
    return render_template('cus_select.html')

app.run(debug=True)