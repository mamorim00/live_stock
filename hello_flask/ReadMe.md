
What we will use:
Flask: microramework for python web applications
HTMl: for our templates
Jinja 2: helps us create templates in html with python
JS: a tiny bit of java script to autoupdate the page
CSS: Just to see the table properly
Python: create our small web app and make the API calls

Steps:


step 1:

-Find API
-Figure out how to make Api Call
-Return values as Json

step 2:
-understand the Json object
-find a way to send it to the frontend 
-We can use Flask -> fast to write code and simple

step 3:
-how can I send the values to front end?
-Use to do it
-Add to the tables using Jinja 2
-create two pages : forex and crypto for each table and switch betwen them with buttons
-How to autoupdate? make a call every minute? 

step 4:
-autoupdate works
-Datails to fix:
     -make spread absolute value of conversion of the response from str to float and display w/ 2 digit precision
     -




Problems to be adressed:

- The basic version of the API only allows 5 calls per minute so we have to autoupdate every two minutes and cannot switch from one table to another

- why reload all page? only thing in our page is the table

