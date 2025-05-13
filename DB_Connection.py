import pymysql

# Function to connect to locally hosted database
def get_conn():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root', 
        password = 'Lordm0ngrel?',
        database = 'articlesummarize'
        )
    return conn