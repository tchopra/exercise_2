import sys
import psycopg2

# @TC connect to the database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# @TC Establish the connection with database tcount
cur = conn.cursor()

SQL = "SELECT * FROM tweetwordcount WHERE count >= %s and count <= %s ORDER BY word ASC;"
parm1 = str(sys.argv[1])
parm2 = str(sys.argv[2])
data = (parm1, parm2)

cur.execute(SQL, data)
Qresult = cur.fetchall()
conn.commit()
#@TC close the connection with database tcount
conn.close()

#print records from the query one at a time.
for record in Qresult:
    print record
