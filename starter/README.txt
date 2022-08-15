

$ cd capstone
$ source cap/bin/activate
$ cd starter
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run


==============
Prep for database

1.  createdb capstone
    createdb capstone_test

2.  flask run --reload   (this should create empty tables)

3.   $ cd starter/dbscripts
     $ psql -U postgres capstone < choir.sql
        Password for user postgres:
        INSERT 0 1
        INSERT 0 1
        INSERT 0 1

    $  psql -U postgres capstone < singer.sql
    $  psql -U postgres capstone < enrollment.sql

4.  $ cd starter
     $ mv migrations migration-orig
     $ flask db init
     $ flask db migrate -m "initial migration"


===========
recreate database

1.
capstone=# delete from enrollment;
DELETE 17
capstone=# select * from enrollment;
 id | choir_id | singer_id
----+----------+-----------
(0 rows)

capstone=#

2.  capstone=# delete from choir;

3.  capstone=# delete from singer;

4.  stop flask

5.  switch user to postgres
    $ dropdb capstone

6.  createdb capstone
    createdb capstone_test

7.  uncomment both forieng keys in class ChoirEnrollment

8.  flask run --reload   (this should create empty tables)

9.   $ cd starter/dbscripts
     $ psql -U postgres capstone < choir.sql
        Password for user postgres:
        INSERT 0 1
        INSERT 0 1
        INSERT 0 1

    $  psql -U postgres capstone < singer.sql
    $  psql -U postgres capstone < enrollment.sql

10.  $ cd starter
     $ mv migrations migration-orig
     $ flask db init
     $ flask db migrate -m "initial migration"



list singer information for signers in first page
$ curl http://localhost:5000/singers -H "Accept: application/json" -H "Authorization: Bearer $singer_token"

list singer information for singers in paginated page 2
$ curl -X GET http://localhost:5000/singers\?page\=2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token

list singer information by singer_id = 2
$ curl -X GET http://localhost:5000/singers/2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token"

list singer name in specified voice part (alto)
$ curl -X GET http://localhost:5000/singers/alto -H "Accept: application/json" -H "Authorization: Bearer $singer_token"

add a new singer




Domain:         sywong10chorus.us.auth0.com
API Audience:   chorus
Client ID:      taUeqV5y7Egh7g6Kf9P57j2zTDpLucmU
Allowed Callback URLs:  https://localhost:8080/login-result


directory
sywong109@gmail.com
Hoboken10!

https://sywong10chorus.us.auth0.com/authorize?audience=chorus&response_type=token&client_id=taUeqV5y7Egh7g6Kf9P57j2zTDpLucmU&redirect_uri=https://localhost:8080/login-result
https://localhost:8080/login-result#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ5NVJqMVUwdUd0NFJvcjI1VGtpRiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZzEwY2hvcnVzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmRjNmNiN2U1MThlYmI2Nzc1ZWIyMWYiLCJhdWQiOiJjaG9ydXMiLCJpYXQiOjE2NjA0OTQ4NDIsImV4cCI6MTY2MDU4MTI0MiwiYXpwIjoidGFVZXFWNXk3RWdoN2c2S2Y5UDU3ajJ6VERwTHVjbVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjaG9pcnMiLCJkZWxldGU6c2luZ2VycyIsImdldDpjaG9pcnMiLCJnZXQ6ZW5yb2xsbWVudHMiLCJnZXQ6cGFydCIsImdldDpwYXJ0X2luX2Nob2lyIiwiZ2V0OnNpbmdlcnMiLCJwYXRjaDpjaG9pcnMiLCJwYXRjaDpzaW5nZXJzIiwicG9zdDpjaG9pcnMiLCJwb3N0OmVucm9sbF9zaW5nZXIiLCJwb3N0OnNpbmdlcnMiXX0.KbHB4WaCB2bKMfXVtfK7wQ1Yulda7svQu6B6khAaknhoEczeb1LoFIJDY8KmFivLzThxXDDg3hfQQ6o5FGjDd44zoX2VcYqrKTSHuwuvttz4nNeS6Iawv7aCb-OEY_gJN-RBlR2aOVNV9xXlEnl2HGePut7Y1zUwe_O4pZYzfaI9zwi7KHA2rE4VyNoOu-iU-eCd-Wojim23F8wOJxEWMaRlbQa72HN8xpGipVU9_Jm4-1z3_-iGBGBBLoSCOLqa9TXpxEmR79Hs1k3Xmre3QWnIGL8TiZSnSN9yKDzSdTk6yY-j5si3IRBh9buYG5i2vJp0u7THkMUhFJecc40vCA&expires_in=86400&token_type=Bearer


singer
sywong10@yahoo.com

https://localhost:8080/login-result#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ5NVJqMVUwdUd0NFJvcjI1VGtpRiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZzEwY2hvcnVzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmRjNmQ3ZTM1Yzk5ZGM4YjhjNjczMDIiLCJhdWQiOiJjaG9ydXMiLCJpYXQiOjE2NjA0ODkzNDQsImV4cCI6MTY2MDU3NTc0NCwiYXpwIjoidGFVZXFWNXk3RWdoN2c2S2Y5UDU3ajJ6VERwTHVjbVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzaW5nZXJzIiwiZ2V0OmNob2lycyIsImdldDplbnJvbGxtZW50cyIsImdldDpzaW5nZXJzIiwicGF0Y2g6c2luZ2VycyIsInBvc3Q6c2luZ2VycyJdfQ.pXpMitJ_jEBvmGYydm2B0e6_LdsoN9dS1yimakNWyRRKPyXrA-xmsdBfwfSy6pC2ljl6Q4qTHBr8GgJnn1Gw4dpuj4wmfF7YfF-LCFlwbrGWcxqxsUeYGgl8LM1aQGFkmMAzTo2Ut1WIQWGzt-kQc1wAlrtBsVTI4IVVvU4bOE9K5YcV_j_iU-23OcPuezl5fBC-H6GDpPrjLMAh0HBuj3XnINyZgRsY5d76-Op9z-PvuVyOz-t6y3C8ZNxbs49gQYR3S95ejbYspDK2muj5fof09NpdyTL-xNwlebdIezRKUDE8AxsaYEoPFSxtxGw6VafuWOt2mKwIB_LVkFJ1-Q&expires_in=86400&token_type=Bearer

