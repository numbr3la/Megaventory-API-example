# Synopsis
This is example of web application which uses of Megaventory REST API to cloud inventory management.


# How it works
File config.ini contains basic configuration of web app. Parameters such as address of host, web application port and Megaventory API token can be set here.

![image](https://user-images.githubusercontent.com/74925191/177056567-e936279d-fa53-4b1a-82ef-a7391a473da6.png)

To run the application, you have to call Main.py Then, app should start on the chosen port. If you open web application website in your browser, you should see elementary page like this:

![image](https://user-images.githubusercontent.com/74925191/177056219-2fd7c962-936e-4d36-94d4-abfe2f6dbbc2.png)

If you click the 'Test' button, you will be redirected to localhost/test/ and then, app runs src/Test.py. The task of the test is to create several entities and save them in Megaventory base by REST API. For this purpose, app creates step by step desired entities with specified parameters and inserts them by HTTP methods to REST API endpoints. Due to the different structure of the queries, every main key of the endpoint has its file with functions handling different requests. After inserting the entity, if it is necessary, app gets values from response and updates local entities. At the end of test, you should see text

![image](https://user-images.githubusercontent.com/74925191/177057386-124a744c-b2ee-4825-8456-339a5112b8b1.png)

If your parameters are incorrect and any error occurs, you can notice that in your console.


# Reference project
So far, I have never worked with this kind of project. 


# Technologies
Python 3.7, 
Flask 2.1.2, 
SQLAlchemy 1.4.39
