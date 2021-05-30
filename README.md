# **API Use Guide**

### [Base Route](jensenry.pythonanywhere.com/)
Add one of below routes to base url to make a call. Make sure there is a  trailing ‘/’ at the end (Ex.  jensenry.pythonanywhere.com/pets/)

### admin/
-Admin page, can log in as a superuser and view or alter any entries in the database
-This isn’t actually an API route callable by the frontend- it just provides a UI to see the database

### api/ [GET]
Isn’t actually an api call you’d use. But while debugging it does have a nice UI to click around the API and follow hyperlinks to endpoints.

### api/ [GET]
Isn’t actually an api call you’d use. But while debugging it does have a nice UI to click around the API and follow hyperlinks to endpoints.

### api/pets/ [GET, POST]
- Get - Returns all Pet objects in the database
- Post - Allows to post a pet to the database (You need to have a valid JWT in the header of the API call as Authorization: Bearer <key>, which you can get by logging in and copying the key returned from the api/login/ route. (Otherwise if you just want to experiment for now, it may be easier to add pets through the admin panel.)


