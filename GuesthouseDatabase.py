import sqlite3
#backend



def hotelData():
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Guesthouse (id INTEGER PRIMARY KEY, CusID text,Firstname text,Surname text,Address text, \
        Gender text,Mobile text,Nationality text,ProveOfID text,DateIn text,DateOut text)")
    con.commit()
    con.close()

def addHotelRec(CusID, Firstname,Surname,Address,Gender, Mobile,Nationality,ProveOfID,DateIn,DateOut):
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Guesthouse VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)", \
                (CusID, Firstname,Surname,Address,Gender, Mobile,Nationality,ProveOfID,DateIn,DateOut))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Guesthouse")
    rows=cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Guesthouse WHERE id=?", (id,))
    con.commit()
    con.close


def searchData(CusID="", Firstname="",Surname="",Address="", Gender="",Mobile="", Nationality="", ProveOfID="", DateIn="", DateOut=""):
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Guesthouse WHERE CusID=? OR Firstname=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? \
                OR Nationality=? OR ProveOfID=? OR DateIn=? OR DateOut=?", \
                (CusID, Firstname,Surname,Address,Gender, Mobile,Nationality,ProveOfID,DateIn,DateOut))
    rows=cur.fetchall()  
    con.close()
    return rows 
    
def dataUpdate(id,CusID="", Firstname="",Surname="",Address="", Gender="",Mobile="", Nationality="", ProveOfID="", DateIn="", DateOut=""):
    con=sqlite3.connect("Guesthouse.db")
    cur = con.cursor()
    cur.execute("UPDATE Guesthouse SET CusID=?, Firstname=?,Surname=?,Address=?, Gender=?, Mobile=?, Nationality=?, ProveOfID=?,DateIn=?,DateOut=?,WHERE id=?", \
                (CusID, Firstname,Surname,Address,Gender, Mobile,Nationality,ProveOfID,DateIn,DateOut,id))
    con.commit()
    con.close()



 

hotelData()



