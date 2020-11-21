import psycopg2 as pg

Database_url = 'postgres://yctlzmuuxmgyeo:8e1474edfd4c01994ff7f8b496b9fc3619f1c3e1f312b36e2295b0eb9a8aa85a@ec2-18-203-62-227.eu-west-1.compute.amazonaws.com:5432/d3v85adstclkte'

db = pg.connect(Database_url,sslmode='require')

connection = db.cursor()
if connection:
    print('Connection established')
else:
    print('Connection Failed')

def create_user():
    connection.execute('''CREATE TABLE IF NOT EXISTS Data(
        FirstName text NOT NULL,
        LastName text,
        emailaddress varchar NOT NULL UNIQUE,
        Username varchar NOT NULL UNIQUE,
        password varchar NOT NULL
    )''')

def add_user_data(first_name,last_name,emailaddress,user,password):
    connection.execute('''INSERT INTO Data(FirstName,LastName,emailaddress,Username,password) values (?,?,?,?,?)''',(first_name,last_name,emailaddress,user,password))
    db.commit()
def display_data():
    connection.execute('''SELECT * FROM Data''')
    rows = connection.fetchall()
    return rows
def delete_data():
    connection.execute('''delete from Data''')
    print('Deleted Successfully')
    db.commit()
def column_data(column_name = None):
    if column_name == 'emailaddress':
        connection.execute('''select emailaddress from Data''')
        col = connection.fetchall()
        return col
    elif column_name == 'username':
        connection.execute('''select Username from Data''')
        col = connection.fetchall()
        return col
    else:
        connection.execute('''select * from Data''')
        rows = connection.fetchall()
        return rows
def two_columns_retrieval(user,passe):
    connection.execute('''select * from Data where Username=? and password=?''',(user,passe))
    rows =  connection.fetchall()
    return rows