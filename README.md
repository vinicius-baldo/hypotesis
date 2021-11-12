# hypotesis
For the assessment and the interview.

Some explanation on why I made some decisions

1 - This is mostly a django/API implementation of what was specified in the document. While the description of the document suggested a more
tradicional application (instead of a web one). My questioning with the recruiter indicated that the position was for someone with knowledge of python/django
so this is why i did this way.

2 - The decision was made to consider if a username is sent on a transaction, the system should try to recover that user and if does not exists, 
create a new one with that information. I used django User model for this. On a production enviroment this should probably be changed to a custom one

3 - While it was not specified on the document, I decided to not allow a transaction from a user to itself

4 - To run, execute python3 manage.py runserver, this will enable the application at http://127.0.0.1:8000/

5 - It is possible to run some test using only the web interface. 
    Opening http://127.0.0.1:8000/ledger/transaction/process/ will bring a web interface to send the data.
    To create a Transaction add to the content field {"transaction": "2015-01-16,john,mary,125.00"}
    To recover data from a user to a certain data use http://127.0.0.1:8000/ledger/transaction/<username>/<date>/
    as in http://127.0.0.1:8000/ledger/transaction/john/2021-11-11/

6 - Automated tests can be run using python3 manage.py test. I created one test that does multiple assertions. On a production enviroment
    it would be better to break them and test each feature on its on testcase.
