# Petsitters

A little Pet-Sitters Django app that I coded up as part of an interview screening. Fun.

## Install dependencies
run 

`pip install -r requirements.txt` 

to install all dependencies. 

## Loading (and Clearing) Data

First run the migrations:

`python manage.py migrate`

to load the schema into the DB, and then to load up test data into the local sqlite instance, run:

`python manage.py runscript import_data`

to import data from the CSV file.  To remove all of the model data, run:

`python manage.py runscript delete_data`

I added django-extensions for `runscript` support (https://goo.gl/auAuFv) so that I 
can import data / run a script in Django server context (for the rebuild data step).

## Running my tests

I didn't have time for great test coverage, but:

`python manage.py test`

will run the unit tests I have; and one level above the manage.py stuff you can run:

`python functional_tests.py`

which runs a simplistic Selenium-based functional/ E2E style test (I'd do more of these with some time).

## View the Sitters

As you can imagine, to view the site, just run:

`python manage.py runserver`

to see a list of sitters at http://localhost:8000.  It displays the list and info as requested although
I didn't have time to do nifty client-side javascript filtering of data by rating/rank (I've done this kind
of thing before with KnockoutJS and Angular but... time).

Also it is a bit weird that we display sitters by rank but only display average rating... could be confusing
for users.  But that is what the instructions called for.

best - Michael


