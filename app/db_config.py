import psycopg2
import os


DB_HOST = 'localhost'
DB_USERNAME = 'postgres'
DB_PASS = 'tomkin254'
DB_NAME = 'ireporter'
DB_PORT = '5432'


url = "dbname='ireporter' host='localhost' port='5432' user='postgres' password='tomkin254'"


db_url = os.getenv('DATABASE_URL')

print(db_url)

#create connection
con = psycopg2.connect(url)

#create the cursor
cur = con.cursor()

con.close()