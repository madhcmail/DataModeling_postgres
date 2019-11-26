# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id serial PRIMARY KEY,\
                start_time varchar,user_id varchar,level varchar,song_id varchar, artist_id varchar, \
                session_id int, location varchar,user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id varchar PRIMARY KEY,first_name varchar,\
                    last_name varchar,gender char,level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY, title text, \
                    artist_id text,year int,duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists ( artist_id text PRIMARY KEY, name varchar,\
                        location text, latitude numeric, longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time varchar,hour int, day int,week int, month int,\
                        year int,weekday int);""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays(songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)ON CONFLICT(songplay_id) DO NOTHING""")

user_table_insert = ("""INSERT INTO users(user_id,first_name,last_name,gender,level)values(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO NOTHING""")

song_table_insert = ("""INSERT INTO songs(song_id,title,artist_id,year,duration)VALUES(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists(artist_id,name,location,latitude,longitude)values(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING """)


time_table_insert = ("""INSERT INTO time(start_time,hour,day,week,month,year,weekday) values(%s,%s,%s,%s,%s,%s,%s) """)

# FIND SONGS
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.

song_select = ("""SELECT song_id,artists.artist_id FROM songs JOIN artists ON artists.artist_id = songs.artist_id
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]