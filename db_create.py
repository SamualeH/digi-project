'''
  Creating database tables
'''

import sqlite3
from sqlite3 import Error  #lets you display errors


def db_tables(conn):
    


    c = conn.cursor()  #making cursor object

    c.execute(""" CREATE TABLE IF NOT EXISTS players (
            name DATATYPE text
            )"""
     )

    c.execute(""" CREATE TABLE IF NOT EXISTS quizes (
            score DATATYPE integer,
            q1 DATATYPE text,
            q2 DATATYPE text,
            q3 DATATYPE text,
            q4 DATATYPE text,
            q5 DATATYPE text,
            q6 DATATYPE text,
            q7 DATATYPE text,
            q8 DATATYPE text,
            q9 DATATYPE text,
            q10 DATATYPE text
            )"""
     )


    c.execute(""" CREATE TABLE IF NOT EXISTS games (
            games_played DATATYPE integer
            )"""
     )


# step 3 - display players in db table
def search_db_players():
    c.execute("SELECT rowid,* FROM players")  #showing row id and other fields
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()

    for i in results:    # this will display the tuples in the list
         print(i)      

# display percent of players that got questions right
def search_db_percent():
    divide_by = 0
    c.execute("SELECT name FROM players")
    results = c.fetchall()   #you can use fetchone if you want one result
    conn.commit()

    for i in results:
        divide_by += 1

    divide = 0
    c.execute("SELECT q1 FROM quizes")
    results = c.fetchall()   #you can use fetchall if you want one result
    conn.commit()

    for i in results:
        divide += 1

    divide_result = divide / divide_by
    print(divide_result) # correct answers DIVIDED BY players times 100

#display percent of questions that the player got rights


#---main ----------
conn = None   

try:
  conn = sqlite3.connect("quiz_game.db")  #or type straight in 
except Error as e:
  print(e)

# step 1 making the database and tables  
db_tables(conn) #run the create tables code
c = conn.cursor()  #making cursor object

# step 2 making a player in the database
name = input('Enter your name: ')
# putting players name into player table
c.execute("INSERT INTO players VALUES ('{}')".format(name))


# step 3 - display players in db table     
search_db_players()

search_db_percent()





















