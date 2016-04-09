import sys
import psycopg2

# @TC connect to the database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# @TC Establish the connection with database tcount
cur = conn.cursor()

SQL = "SELECT count FROM tweetwordcount WHERE word = %s;"
word_desc = str(sys.argv[1])
data = (word_desc,)

cur.execute(SQL, data)
Qresult = cur.fetchone()
conn.commit()
#@TC close the connection with database tcount
conn.close()

print 'Total number of occurences of ', str(sys.argv[1]), ': ', Qresult[0]

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv[1])
