
**Capstone - Chorus project**


The Capstone - Chorus project is a final project of Full Stack Web Developer Nanodegree of Udacity.

* Chorus project is an application to help singers in nearby counties to let choral directors know their availability.
Singers can register themselves to a local registry with information of their voice part, their availability for rehersal days and phone number for communication.

* Choral directories can use this information to assemble their choral groups per singers' voice parts and rehearsal availability.


**Models**

singer table with colums name, phone, voice_part, not_available
choir table with columns name and practice_time

enrollment table with enrollment_id, choir_id and singer_id


**Endpoints**

**GET** <br />
  /singers  <br />
  /singers/<int:singer_id> <br /> 
  /singers/<voice_part> <br /> 
  /choirs <br /> 
  /choir/<int:cid> <br /> 
  /choir/<int:cid>/<s_voice_part> <br />


**PATCH** <br />
  &nbsp;&nbsp;/singers/<int:id> <br /> 
  &nbsp;&nbsp;/choirs/<int:id> <br />

**POST** <br />
  /singers <br /> 
  /choirs <br /> 
  /enroll/<choir_name>/<int:sid> <br />

**DELETE** <br />
  /singers/<int:id> <br /> 
  /choirs/<int:id> <br />


**Roles** <br />

* singer: can register singer, unregister singer, update singer information, view list of people who have registered, list of people enrolled in each choir.
* director: can do everything singer can.  Director also can enroll and unenroll a singer to a chorus according to their voice part and availability.


**setup Python environment**

$ cd capstone
$ pip install -r requirements.txt
$ source cap/bin/activate
$ cd starter
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run --reload


**Prep for database**


1.  createdb capstone
    createdb capstone_test

2.  flask run --reload   (this should create empty tables)

3.   $ cd starter/dbscripts
     $ psql -U postgres capstone < choir.sql
     $ psql -U postgres capstone_test < choir.sql
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

    

**recreate database**

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

     

**curl example to some endpoints**


list singer information for signers in first page
$ curl http://localhost:5000/singers -H "Accept: application/json" -H "Authorization: Bearer $singer_token"

list singer information for singers in paginated page 2
$ curl -X GET http://localhost:5000/singers\?page\=2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token

list singer information by singer_id = 2
$ curl -X GET http://localhost:5000/singers/2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token"

list singer name in specified voice part (alto)
$ curl -X GET http://localhost:5000/singers/alto -H "Accept: application/json" -H "Authorization: Bearer $singer_token"


**Error Code**

401 - authorization header, token issue
403 - not authorized
404 - resource not found
409 - schedule conflict
422 - unprocessable_entity


**API endpoints**
http://localhost:5000


**GET /singers**









Domain:         sywong10chorus.us.auth0.com
API Audience:   chorus
Client ID:      taUeqV5y7Egh7g6Kf9P57j2zTDpLucmU
Allowed Callback URLs:  https://localhost:8080/login-result


directory
sywong109@gmail.com
Hoboken10!

https://sywong10chorus.us.auth0.com/authorize?audience=chorus&response_type=token&client_id=taUeqV5y7Egh7g6Kf9P57j2zTDpLucmU&redirect_uri=https://localhost:8080/login-result
https://localhost:8080/login-result#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ5NVJqMVUwdUd0NFJvcjI1VGtpRiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZzEwY2hvcnVzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmRjNmNiN2U1MThlYmI2Nzc1ZWIyMWYiLCJhdWQiOiJjaG9ydXMiLCJpYXQiOjE2NjA1ODU3ODIsImV4cCI6MTY2MDY3MjE4MiwiYXpwIjoidGFVZXFWNXk3RWdoN2c2S2Y5UDU3ajJ6VERwTHVjbVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjaG9pcnMiLCJkZWxldGU6c2luZ2VycyIsImdldDpjaG9pcnMiLCJnZXQ6ZW5yb2xsbWVudHMiLCJnZXQ6cGFydCIsImdldDpwYXJ0X2luX2Nob2lyIiwiZ2V0OnNpbmdlcnMiLCJwYXRjaDpjaG9pcnMiLCJwYXRjaDpzaW5nZXJzIiwicG9zdDpjaG9pcnMiLCJwb3N0OmVucm9sbF9zaW5nZXIiLCJwb3N0OnNpbmdlcnMiXX0.OAeprtMFR1RiUWWCoc6Tqp0fkdTgYKm3qP7kJmDi4hhPMivOGYV4XgtH6jpfpsHqX3-8DQTMI3vQ6EvQyqVi2mXZN8oqzz7fs368oZ9UqvPnBAUI1O518bOb_JrUHsuLHmiCkKeykqUkOQd-R4L4uDA98QYd08w_1vzAIjwCBaOMeUHiw-IhzNKPVAJWINh9tofhi3ljMXnFYndHMPTZm5z7upimriDsWdws7boSjRMzXPPC-yNF80ygfwM2vsFAvZCs0QW9L6nHe1UG9l4YQQeYpX_thzbdzzPXr8huxCDWDFZXd4tFOt5yLBkgogFI02a2QeB4PsFdEx4Anf_VPg&expires_in=86400&token_type=Bearer


singer
sywong10@yahoo.com

https://localhost:8080/login-result#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ5NVJqMVUwdUd0NFJvcjI1VGtpRiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZzEwY2hvcnVzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmRjNmQ3ZTM1Yzk5ZGM4YjhjNjczMDIiLCJhdWQiOiJjaG9ydXMiLCJpYXQiOjE2NjA1ODU2ODQsImV4cCI6MTY2MDY3MjA4NCwiYXpwIjoidGFVZXFWNXk3RWdoN2c2S2Y5UDU3ajJ6VERwTHVjbVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzaW5nZXJzIiwiZ2V0OmNob2lycyIsImdldDplbnJvbGxtZW50cyIsImdldDpzaW5nZXJzIiwicGF0Y2g6c2luZ2VycyIsInBvc3Q6c2luZ2VycyJdfQ.mvG9XvPbLR2xT6i7DVUMjzFLpNvEGt-vwErNru-3JlW14KlUwUDFQ-u68jdx76NyaQCgePwpmZHdPZ-nI1mtLlQdD6I1p56JbIY9b-OciiDD67vWdrBT9hcAndpnX8ejneynPKBbC3RTlUA0wYI6sU8qnwXUgaWtP4zux69V1UI82Hb3A3jmn69W13-ckL7jeO3R1zZGYwSwZvqdf9lOEe-nxPlocdapw5v53vn4sQ0LNAMTAlNSMn_ydxiZ0lJhuYW8ABvDHx0Z1pSC1aMwM2LRb-xTDIpt0f8CSPxklddTVrXRkedQsj0hdDu8O6OY5MPgsLrkNRXNoXpKl9t66A&expires_in=86400&token_type=Bearer

