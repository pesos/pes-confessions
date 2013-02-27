pes-confessions
===============

App to search by Confession # on the PES-Confessions Facebook page. 

This was a quick hack and has a lot of issues. 
FBlogger.py - Used for logging. Fetches upto 300 of the latest confessions and adds it to a mongo collection as {confID: <Confession Number>, message: <body of the post>}

main.py - Simple Python Flask server that gets the confession number from the URL (http://<HOST>/<Confession Number>) and searches the mongo collection for the confession. 

Known issues: 
1. FBlogger does not run periodically and pagination is not handled. Modify the script to run automatically every X mins. 
2. Some problem with unseen confession IDs. Flask is not returning the response text properly. 

Add features and send a pull request! 
