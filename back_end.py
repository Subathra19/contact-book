import sqlite3

def connect():
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, address TEXT, contact INTEGER)")
    con.commit()
    con.close()
    
def insert(first_name,last_name,gender,address,contact):
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("INSERT INTO contact VALUES(NULL,?,?,?,?,?)",(first_name,last_name,gender,address,contact))
    con.commit()
    con.close()
    
def view():
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM contact")
    data=cur.fetchall()
    con.commit()
    con.close()    
    return data

def search(first_name="",last_name="",gender="",address="",contact=""):
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM contact WHERE firstname=? or lastname=? or gender=? or address=? or contact=?",(first_name,last_name,gender,address,contact))
    data=cur.fetchall()
    con.commit()
    con.close()    
    return data

def update(id,first_name,last_name,gender,address,contact):
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("UPDATE contact SET firstname=?, lastname=?, gender=?, address=?, contact=? WHERE id=?",(first_name,last_name,gender,address,contact,id))
    con.commit()
    con.close()  

def delete(id):
    con=sqlite3.connect("contacts.db")
    cur=con.cursor()
    cur.execute("DELETE FROM contact WHERE id=?",(id,))
    data=cur.fetchall()
    con.commit()
    con.close()   

connect()
