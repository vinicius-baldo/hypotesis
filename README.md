# hypotesis
For the assessment and the interview.

Some explanation on why I made some decisions

1 - This is mostly a django/API implementation of what was specified in the document. While the description of the document suggested a more
tradicional application (instead of a web one). My questioning with the recruiter indicated that the position was for someone with knowledge of python/django
so this is why i did this way.

2 - The decision was made to consider if a username is sent on a transaction, the system should try to recover that user and if does not exists, 
create a new one with that information 

3 - While it was not specified on the document, I decided to not allow a transaction from a user to itself
