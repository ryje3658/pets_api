# pets_api
API backend for pets application for Capstone.

API use guide


BASE ROUTE: jensenry.pythonanywhere.com/
Add to base to make a call and make sure there is a  trailing ‘/’ at the end (Ex.  jensenry.pythonanywhere.com/pets/)

Routes
admin/
Admin page, can log in as a superuser and view or alter any entries in the database
This isn’t actually an API route- it just provides a UI to see the database
api/ [GET]
Isn’t actually an api call you’d use. But while debugging it does have a nice UI to click around the API and follow hyperlinks of data.
api/pets/ [GET], [POST]
Get - Returns all Pet objects in the database
Post - Allows to post a pet to the database (You need to have a valid JWT in the header of the API call as Authorization: Bearer <key>, which you can get by logging in and copying the key returned from the api/login/ route. (Otherwise if you just want to experiment for now, it may be easier to add pets through the admin panel.)
api/pets/<insert query param to filter by breed, type, availability, disposition> [GET]
So you send the request to api/pets/ and then in the query params you’d put either breed, type, availability, or disposition and then the request would return the Pets filtered by the value you gave it (example below would return all animals of breed “CuteCat”)

api/pets/<int:id>/ [GET, PUT, PATCH, DELETE]
Refers to a single Pet object in database 
api/users/
Returns all users
api/users/<int:id>/
Returns one User object with the provided id number
api/login/ [POST]
Receives a username and password, returns JWT (JSON web token) access keys
api/login/refresh/ [POST]
Refreshes access tokens- not sure if important
api/register/ [POST]
Receives username, email, password, confirm password and registers that user into the database if all given information is valid, should return relevant errors if bad information is given (a non unique email or username, weak password, etc.)
api/registershelter/ [POST]
Receives username, email, password, confirm password and registers that user into the database as above route, but will also update the User’s profile to be a shelter and will use the username field as the name of the shelter
