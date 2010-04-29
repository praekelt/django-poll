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
    
Poll model extends content.models.ModelBase. Add a poll to the CMS.
Linked to multiple poll options via a foreign key and associated to a content entry via ModelBase ManyToMany.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
content
    ManyToMany field to ModelBase linking polls to content entries. Polls can be associated to multiple entries.
extends django-content fields
    See django-content README

METHODS
*******
None

MANAGERS
********
None

PollOption:
-----------
class models.PollOption
    
PollOption model extends content.models.ModelBase. Associated with poll object via foreign key.
Content objects can be used as poll options or a standard text option can be used.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
title
    Char field with title of poll option, if not selected the content objects title will be used instead.
poll
    Foreign key to poll object
content
    Foreign key to content object via ModelBase
correct_answer
    Boolean field denoting if the object is the correct answer.

METHODS
*******
save::
    PollOption.save()
Save the content object's title if a title has not been specified

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
