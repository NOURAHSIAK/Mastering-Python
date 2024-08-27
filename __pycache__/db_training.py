import sqlite3

def get_all_data():
    try:
        #connect to data base
        db = sqlite3.connect("app.db")
        #setting up the cursor
        cr = db.cursor()
        #fetch data from database
        cr.execute("select * from users")
        #assign data to variable
        results = cr.fetchall()
        #print number of rows
        print(f"Data base has {len(results)} rows")   
        #showing data
        print("showing data:")
        for row in results:
            print(f"user_id => {row[0]},", end=" ")
            print(f"user_name => {row[1]}")
    except sqlite3.Error as er:
        print(f"Error reading data: {er}")
    finally:
        if (db):
            db.close()
            print("connection to dta base is closed")
get_all_data()