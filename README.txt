Concert Video Catalog

A catalog containing concert videos released by artists and bands.

All logged in users can add new artists and new videos.  Logged in users can 
also update all artists and all videos.  Only users who created the artist and 
video can delete them.

All logged in users can add, update and delete tracks for all videos.  There's 
no restriction on deleting tracks.

The application is written in Python 2 and uses the Flask framework.

Before using the following files must be executed in terminal:

python db_setup.py
python load_db.py

These commands will setup and load the sqlite database.

To run the application, enter the following command in terminal:

python application.py

Third-party authentication and authorization is implemented by using Google Accounts.
You must have a google account to login.  You can still view the catalog without 
logging in.

The file oauth_google.json file contains the API credential information.  The 
"client_secret" value has been removed and you need to use your own.

Thanks to https://github.com/udacity/ud330/tree/master/Lesson4/step2 for assistance 
with project and Google Sign-In documentation https://developers.google.com/identity/sign-in/web/.


