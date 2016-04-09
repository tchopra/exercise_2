#Name: Tarun Chopra
#Section: w205
#Purpose: It will take the valid words from the tweet that were being
#parsed by the parse.py bolt and then will perform the following steps.
# 1. Connect to the tcount postgres database.
# 2. Parse the word, increment the word count.
# 3. If word count is 1, then insert a new entry into the tweetwordcount
#    table.
# 4. If the word count is >1, then update the count of the already existing
#    word in the tweetwordcount table.

from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2 #@TC

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        #self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # connect to the database
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # Establish the connection with database tcount
        cur = conn.cursor()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # if count is 1 then insert a new entry and if the count is more
        # than 1 then update the existing entry.

        if self.counts[word] == 1 :
            #Insert a new entry into the table
            SQL = "INSERT INTO tweetwordcount (word, count) VALUES (%s, %s);"
            data = (word, self.counts[word])
            cur.execute(SQL, data)
            conn.commit()
        else:
            #update the new entry into the table
            SQL = "UPDATE tweetwordcount SET count=%s WHERE word =%s;"
            data = (self.counts[word], word)
            cur.execute(SQL, data)
            conn.commit()

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        #close the connection with database tcount
        conn.close()
