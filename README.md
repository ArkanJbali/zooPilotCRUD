# ZooPilot
> Web API with Python, Flask, and [MongoDB](https://www.mongodb.com).
ZooPilot is an online course, operated by Tsofen organization, in cooperation with IBM.
key feature of this course to learn NoSQL emphasis on MongoDB.
 - CRUD operations to read and write documents within collections. Discover how to create and manage documents.
 - How MongoDB can be queried, manipulated, and managed with Python.

[![License](https://img.shields.io/github/license/ArkanJbali/zooPilot)](LICENSE) [![Issues](https://img.shields.io/github/issues/ArkanJbali/zooPilot)](https://github.com/ArkanJbali/zooPilot/issues)

## Introduction
#### What Is A Web API?
 - Intro to Web APIs with examples
#### MongoDB:
 - Intro to MongoDB
 - Installation and starting a server
#### Flask:
 - Intro to Flask
 - Flask-RESTful {for building REST APIs}
#### Postman:
 - Intro to Postman
 - Sampling data and using GET, PUT, POST, DELETE requests


#### What Is A Web API?
**A Web API (Application Programming Interface)** allows you to serve data over the web, typically in JSON or XML format. Generally, this is done by exposing endpoints to make requests.
An example is the [PokéAPI](https://pokeapi.co/), which gives you access to a Pokemon database. Try the link below to get all the data you could ever want to know about a Squirtle!
> https://pokeapi.co/api/v2/pokemon/squirtle

By convention, an API will have one entry point. This is like the root folder in your File Explorer. There can be any number of endpoints.
Data can be delivered in different forms depending on the given route. Try navigating to the /pokemon route and you will get the data for ALL Pokemon, instead of just for Squirtle.

#### MongoDB:
##### Intro to MongoDB
hoosing the right type of database for your project is incredibly important. A traditional SQL database stores information in tables. This is in contrast to a noSQL database.
MongoDB is a noSQL database which stores data in JSON format. As opposed to tables, JSON forms a tree data structure. The individual records are known as 'documents'.
Installation and starting a server:
You can get the free version of MongoDB at 
> https://www.mongodb.com/download-center/community

Launch Server: C:\Program Files\MongoDB\Server\4.2\bin\mongod.exe
Leave your server running in the background, you can now access your database from the mongo shell or as we will see later, also from python. This is an unsecured server.
Launch Mongo Shell:
> *C:\Program Files\MongoDB\Server\4.2\bin\mongo.exe*

#### Flask
**Flask is a light-weight web framework**. With Flask, you get to pick-and-choose what components and extension needed for your site.
The main Flask extensions we will use are Flask MongoEngine and Flask RESTful. The first will let us build Classes as templates for our data and the latter is designed for building an API, and makes the process simpler.
Create a clean virtual environment and get Flask.
> pip install Flask

##### Flask-RESTful
> pip install flask-restful

The Flask-RESTful library will require a setup much like MongoEngine, where we will make a Class for each API interaction. These Classes are called Resources. In Flask, connecting a Resource to an endpoint is called a route. This is what we are referring to when we say routes.
Our API will have a few routes. One for authentication (signing up and logging in), another for users (to GET or PUT or DELETE user data), and another for meals (to GET, PUT, or POST).

#### Postman
Rather than explain all of the fun you can have with Postman, I'll step you through signing up, logging in, and adding data. This will get you started, but there's plenty of great features inside.
Download Postman at 
> postman.com/downloads


### Project Structure
```
 │
 │   app.py
 │   README.md
 │
 ├───api
 │       rooms.py
 │       users.py
 │       routes.py
 │       __init__.py
 │
 └───static
 │       css
 │       fontawesome-5.5
 │       img
 │       magnific-popup
 │       slick
 └───templates
 │       index.html
```
