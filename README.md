The project is about a startup company called Sparkify who wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
The analytics team is mainly interested in understanding what songs users are listening to.They do not have an easy way to query the results from the directory of JSON logs they have.As a data engineer, we need to create a Postgres database with tables designed to optimize queries on song play analysis and  build an ETL pipeline for analysis.

The database schema that we use is a star schema to optimize queries on songplay analysis where a fact table songplays is surrounded by a multiple dimension tables(User,songs,artists and time). 

The schema helps the analysts to query the database 

The create_tables.py helps to drop and create the dimensions and Fact tables.
The etl.ipynb notebook is used to build the ETL process for each table.
The etl.py python program is used to process the entire datasets and inserts the records into the dimension and fact tables
sql_queries.py conatins all the queries that we used to create and insert the database tables.
test.ipynb is used to test the queries.

![Database Star Schema](/Scan.pdf)

