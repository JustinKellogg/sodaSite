sodaSite
========

SODA website

Uses:
Python 2.7, Django 1.5, South 0.7.6, jQuery 1.9.1


api: app that handles much of the communication with machines. Contains models used to interact with soda, machines, users and whatnot. 
Communicates with machines by taking url requests (with parameters), performing logic, and returning a json object saying whether the request
was successful. 

blog and polls were tutorials found online which are included for example/reference code. 

jQuery code in place to call a function every x seconds, will use this to check on machines. 

Go to http://south.readthedocs.org/en/latest/tutorial/ for quick tutorials on how to use South for database migration, if necessary. 

Use ./manage.py loaddata data.json, to load data from fixtures in apps (for testing purposes)
