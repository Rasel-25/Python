
from flask import Flask
from flask_restful import Resource, Api
from scrap import WebScrap

app=Flask(__name__) # Creating a app
api=Api(app) # creating a Api

class test(Resource): #creating a class
    def get(self):
        return WebScrap()

api.add_resource(test,"/") # Adds a resource to the api || test the class name of your resource || one or more url routes to match for the resource, standard
app.run(debug=True,port=8888)    # running the app || Runs the application on a local development server.                                                                                             #flask routing rules apply. Any url variables will be passed to the resource method as args. 