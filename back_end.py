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
