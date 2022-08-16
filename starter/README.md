
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
  &nbsp;&nbsp;&nbsp;/singers  <br />
  &nbsp;&nbsp;&nbsp;/singers/<int:singer_id> <br /> 
  &nbsp;&nbsp;&nbsp;/singers/<voice_part> <br /> 
  &nbsp;&nbsp;&nbsp;/choirs <br /> 
  &nbsp;&nbsp;&nbsp;/choir/<int:cid> <br /> 
  &nbsp;&nbsp;&nbsp;/choir/<int:cid>/<s_voice_part> <br />


**PATCH** <br />
  &nbsp;&nbsp;&nbsp;/singers/<int:id> <br /> 
  &nbsp;&nbsp;&nbsp;/choirs/<int:id> <br />

**POST** <br />
  &nbsp;&nbsp;&nbsp;/singers <br /> 
  &nbsp;&nbsp;&nbsp;/choirs <br /> 
  &nbsp;&nbsp;&nbsp;/enroll/<choir_name>/<int:sid> <br />

**DELETE** <br />
  &nbsp;&nbsp;&nbsp;/singers/<int:id> <br /> 
  &nbsp;&nbsp;&nbsp;/choirs/<int:id> <br />


**Roles** <br />

* singer: can register singer, unregister singer, update singer information, view list of people who have registered, list of people enrolled in each choir.
* director: can do everything singer can.  Director also can enroll and unenroll a singer to a chorus according to their voice part and availability.


**setup Python environment**

$ cd capstone <br>
$ pip install -r requirements.txt <br>
$ source cap/bin/activate <br>
$ cd starter <br>
$ export FLASK_APP=app.py <br>
$ export FLASK_ENV=development <br>
$ flask run --reload <br>


**Prep for database**


1.  createdb capstone <br>
    createdb capstone_test <br>

2.  flask run --reload   (this should create empty tables) <br>

3.   $ cd starter/dbscripts <br>
     $ psql -U postgres capstone < choir.sql <br>
     $ psql -U postgres capstone_test < choir.sql <br>
        Password for user postgres: <br>
        INSERT 0 1 <br>
        INSERT 0 1 <br>
        INSERT 0 1 <br>

    $  psql -U postgres capstone < singer.sql <br>
    $  psql -U postgres capstone < enrollment.sql <br>

4.  $ cd starter <br>
     $ mv migrations migration-orig <br>
     $ flask db init <br>
     $ flask db migrate -m "initial migration" <br>

    

**recreate database**

1.
capstone=# delete from enrollment; <br>
DELETE 17 <br>
capstone=# select * from enrollment; <br>
 id | choir_id | singer_id <br>
----+----------+----------- <br>
(0 rows) <br>

capstone=# <br>

2.  capstone=# delete from choir; <br>

3.  capstone=# delete from singer; <br>

4.  stop flask <br>

5.  switch user to postgres <br>
    $ dropdb capstone <br>

6.  createdb capstone <br>
    createdb capstone_test <br>

7.  uncomment both forieng keys in class ChoirEnrollment <br>

8.  flask run --reload   (this should create empty tables) <br>

9.   $ cd starter/dbscripts <br>
     $ psql -U postgres capstone < choir.sql <br>
        Password for user postgres: <br>
        INSERT 0 1 <br>
        INSERT 0 1 <br>
        INSERT 0 1 <br>

    $  psql -U postgres capstone < singer.sql <br>
    $  psql -U postgres capstone < enrollment.sql <br>

10.  $ cd starter <br>
     $ mv migrations migration-orig <br>
     $ flask db init <br>
     $ flask db migrate -m "initial migration" <br>

     

**curl example to some endpoints**


list singer information for signers in first page <br>
$ curl http://localhost:5000/singers -H "Accept: application/json" -H "Authorization: Bearer $singer_token" <br>

list singer information for singers in paginated page 2 <br>
$ curl -X GET http://localhost:5000/singers\?page\=2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token <br>

list singer information by singer_id = 2 <br>
$ curl -X GET http://localhost:5000/singers/2 -H "Accept: application/json" -H "Authorization: Bearer $singer_token" <br>

list singer name in specified voice part (alto) <br>
$ curl -X GET http://localhost:5000/singers/alto -H "Accept: application/json" -H "Authorization: Bearer $singer_token" <br>


**Error Code**

401 - authorization header, token issue <br>
403 - not authorized <br>
404 - resource not found <br>
409 - schedule conflict <br>
422 - unprocessable_entity <br>


**API endpoints**
http://localhost:5000 <br>


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

