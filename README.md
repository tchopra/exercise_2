# exercise_2
Unique word count from real time analysis of twitter streaming.

Step by Step Instruction

1) Need UCBW205Spring2016 image on AWS EC2 instance in order to run this project.

2) Need Twitter Credentials in order to call Twitter API.

3) Modify the file tweets.py in folder exercise_2/tweetwordcount/src/spout and add the user's twitter credentials
      ################################################################################
        # Twitter credentials
      ################################################################################
    twitter_credentials = {
        "consumer_key"        :  "xxxxxxxxxxxx",
        "consumer_secret"     :  "xxxxxxxxxxxx",
        "access_token"        :  "xxxxxxxxxxxx",
        "access_token_secret" :  "xxxxxxxxxxxx",
    }
    
4) Before running the application, create a new data base in postgres call "tcount"

5) Add a table in "tcount" database, call "tweetwordcount" withe following properties.
tcount=# \d tweetwordcount
Table "public.tweetwordcount"
 Column |  Type   | Modifiers 
--------+---------+-----------
 word   | text    | not null
 count  | integer | not null
Indexes:
    "tweetwordcount_pkey" PRIMARY KEY, btree (word)
    
