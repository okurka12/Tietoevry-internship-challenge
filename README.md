# Tietoevry-internship-challenge  
This project is built with the Python Django framework. Since I have no experience with javascript there is no client-side computing being done anywhere at all.

**The app is being used as following:**

 - On the home page (`/`) the user inputs a desired number of table elements and clicks the submit button
 - This sends a POST request to the server, the server saves the number into a cookie and redirects the user to spotify - there the user expresses consens with this app having acces to his library (This is being done every time but next_time spotify sees you gave the consent before and redirects you back immediately)
 - Spotify redirects the user back to this app with a query string containing the authentication code this app needs to request the songs from Spotify API
 - **This is the slowest part** (about 3 s for 1050 songs). There are only 50 songs per request. The app finds out the size of user's library from the first request and sends according number of following requests to obtain all the songs.
 - The app sorts the songs by length and author popularity since those parameters are being sent with the songs from the particular endpoint

**Deployment**

Before deploying, `spotify_analyser/mainapp/tools/spotify_apy.py needs to be edited` so that
 - There is a correct `CLIENT_ID` and `SECRET_KEY` of the registered spotify app
 - `REDIRECT_URI` like so: `domain-name/proceed_with_auth_code/` 
 - These are all constants declared at the beginning of the file

 
