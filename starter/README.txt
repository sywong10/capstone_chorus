
psql -U postgres example < /Users/sallywong/Documents/Sally/classes/udacity/fullstack/FSND/projects/capstone/starter/choir.sql


Prep for database



delete all entries in a table:

capstone=# delete from singer;
DELETE 14
capstone=# select * from singer;
 id | name | phone | voice_part | not_available
----+------+-------+------------+---------------
(0 rows)

capstone=#