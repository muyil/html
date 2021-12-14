import pymysql

####database initialization
#####################
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="Samy0110", database="WillenDafoeDb")

#cursor will execute our sql-scripts
cursor = connection.cursor()

###################################
###################################

####Temperatur
def add_temperature(value, description):
    #standart sql query as a string with the format-function to allow us to use parameters and add a new entry to db.
    query = "INSERT INTO Temperatures (Temperature, Description) VALUES ({},'{}');".format(value,description)
    
    #execute our query within our database
    cursor.execute(query)

    #commit the changes and save the new database entry
    connection.commit()
    print("New meassured Temperature and is added to db")

def get_temperature():
    #standart sql query, get all temperatures from the database
    cursor.execute("SELECT * FROM Temperatures")
    
    #cursor.fetchall() gets as every entry from the cursor.execute query.
    result = cursor.fetchall();
    print("Entries:\n" + result)
    
def delete_full_temparatures():
    #standart sql query, to delete all entries in table
    cursor.execute("DELETE FROM Temperatures")
    
    #save changes
    connection.commit()
    print("Deleted all entries from Temperatures")
    

####Humidity
def add_humidity(value, description):
    query = "INSERT INTO Humidities (Humidity, Description) VALUES ({},'{}');".format(value,description)
    cursor.execute(query)
    connection.commit()
    print("New meassured Humidity is added to db")
    
def get_humidity():
    cursor.execute("SELECT * FROM Humidities")
    result = cursor.fetchall();
    print("Entries:\n" + result)

def delete_full_humidities():
    cursor.execute("DELETE FROM Humidities")
    connection.commit()
    print("Deleted all entries from Humidities")

###Keycard
def add_keycard(value):
    query = "INSERT INTO Keycards (KeyCode) VALUES {};".format(value)
    connection.commit()
    print("Keycard added into db")

def get_keycard(keycard_code):
    #standart sql query with WHERE condition to get only one entry. Use format-function to be able
    #to use parameters.
    query = "SELECT * FROM Keycards WHERE KeyCode = {}".format(keycard_code)
    cursor.execute(query)
    
    result = cursor.fetchall();
    
    #result should only have one entry because each keycode is unique.
    if len(result) == 1:
        return True
    else:
        return False

###User
def add_user(username, password):
    query = "INSERT INTO Users (Username, Password) VALUES ('{}','{}');".format(username,password)
    cursor.execute(query)
    connection.commit()
    print("New user is added to db")

def get_user(user_id):
    query = "SELECT * FROM Users WHERE ID = {}".format(user_id)
    cursor.execute(query)
    result = cursor.fetchall();
    print(result)
    return result

def get_all_user():
    cursor.execute("SELECT * FROM Users")
    result = cursor.fetchall();
    print(result)
    