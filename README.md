# Synopsis
This is example of web application which uses of Megaventory REST API to cloud inventory management.


# How it works
File config.ini contains basic configuration of web app. Parameters such as address of host, web application port and Megaventory API token can be set here.

![image](https://user-images.githubusercontent.com/74925191/177056567-e936279d-fa53-4b1a-82ef-a7391a473da6.png)

To run the application, you have to call Main.py Then, app should start on chosen port. If you open web application website, you should see elementary page like this:

![image](https://user-images.githubusercontent.com/74925191/177056219-2fd7c962-936e-4d36-94d4-abfe2f6dbbc2.png)

If you click 'Test' button, you will be redirected to *localhost/test/* and then, app runs *src/Test.py*. The task of the test is to create several entities with specified parameters and insert them to Megaventory base by REST API. For this purpose, app creates step by step desired entities, inserts them by HTTP methods to REST API endpoints. Due to the different structure of the queries, every main key of endpoint has its file with functions handling different requests.
After inserting the entity, if it is necessery, app gets values from response and update local entities. If your parameters are incorrect and any error occures, you can notice that in your console.

# Reference project
So far, I have never worked with this kind of project. 

# Technologies
Python 3.7
Flask 2.1.2
SQLAlchemy 1.4.39
