Django Poll:
============
**Django polls app.**


Dependancies:
=============
django-content
    git@github.com:praekelt/django-content.git


Models:
=======

Poll:
-----
class models.Poll
    
Poll model extends content.models.ModelBase. Add a poll to the CMS. Linked to multiple poll options via a foreign key.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
extends django-content fields
    See django-content README

METHODS
*******
vote::
    Poll.vote()
Vote method adds a vote count by increment to the option selected by a user.

set_cookie::
    Poll.set_cookie()
Sets a cookie in the users browser if they have successfully voted.

voted::
    Poll.voted()
Check if a user has already voted in a poll by checking the cookies set on their browser

MANAGERS
********
None

PollOption:
-----------
class models.PollOption
    
PollOption model extends content.models.ModelBase. Associated with poll object via foreign key.
Stores the percentage of votes and number of votes places per option.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
poll
    Foreign key to poll object
votes
    Positive integer field storing the number of votes placed on a specific option
percentage
    Float field storing average percentage of votes as calculated by PollOption.save()
extends django-content fields
    See django-content README

METHODS
*******
save::
    Poll.save()
Recalculate the average percentage of all vote options related to the poll object

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
