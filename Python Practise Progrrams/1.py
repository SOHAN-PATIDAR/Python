import mysql.connector as myc

def data_gen():
    con = myc.connect(host='localhost',user='root',password='',db='employees')

    cursor = con.cursor()
    query = 'select * from dept_manager'
    cursor.execute(query)
    for i in cursor:
        yield(i)
        
    
for data in data_gen():
    print(data)
    
  