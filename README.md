Setup Database
================================================================================================================
- Navigate to: https://www.mongodb.com/cloud/atlas
- Signup/Signin to MongoDB using your credentials
- If you signup for the first time, create your cluster based on the instructions given in MongoDB.
     - Once cluster is created, configure your account as instructed on MongoDB.
- Click on collections and select “Add my own Data”. Add “API” to Database name and “book” to Collection name.

Steps to setup venv:
================================================================================================================
Steps to create venv are as below:

- python3 -m venv .venv
- source .venv/bin/activate
- pip install --upgrade pip --no-cache-dir
- pip install -r requirements.txt --no-cache-dir (this will install all the needed packages for you)

Steps needed to run the service:
================================================================================================================
- Once above mentioned steps were executed, run "python application.py”, on success case, below mentioned INFO will 
  be shown on your console:
 * Serving Flask app 'application' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

- As shown on console, service is running on "http://127.0.0.1:5000”, append “/<end points as suggested below>” as a postfix to the url in order 
to see end points of the service.

Available end points:

In order to run any of the CRUD requests,  we need “httpie” module and this will be already installed on your system when you run requirements.txt.

- https://127.0.0.1:5000/api/db_populate —> To populate data into the API->books table on MongoDB.
  Command to populate data into MongoDB is: http POST http://127.0.0.1:5000/api/db_populate

- http://127.0.0.1:5000/api/books —> To see the list of available books info. This end point supports GET and POST requests.
  - Command to GET info from books table: http GET http://127.0.0.1:5000/api/books
  - Command to POST new data to the existing table: echo ‘{“book_id”: “3”, “name”: “Hamlet”, “author”: “Shakespeare”}’ | 
    http POST http://127.0.0.1:5000/api/books

- http://127.0.0.1:5000/api/books/<book_id> —>  To see the info of provided book id. This end point supports GET, PUT and DELETE requests.
  - Command to GET info of particular book id: http GET http://127.0.0.1:5000/api/books/<book_id>
  - Command to PUT/update existing record from book DB is: echo ‘{“book_id”: “3”, “name”: “Hamlet1”, “author”: “William Shakespeare”}’ | 
     http POST http://127.0.0.1:5000/api/books/<book_id>
  - Command to DELETE a record from book DB is: http DELETE http://127.0.0.1:5000/api/books/<book_id>

Steps to Deploy the service
=================================================================================================================
- Navigate to https://aws.amazon.com/ and signup/sign to it.
- In services use, Elastic Beanstalk and select “Create a new environment” and then select: “web server environment”.
- Provide application name and in platform select Python.
- In Application code, select “Upload your code” and in Source code origin, add any suitable Version label and select Local file and upload your .zip file which has the application to deploy.
-  Once the file is successfully uploaded, click on “Create application”.
- This will take some time to upload the application to the cloud and once it is successful, you will be redirected to next page where you can see the status of the deployment.
