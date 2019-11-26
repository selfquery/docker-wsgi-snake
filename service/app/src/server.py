from flask import Flask
from pymongo import MongoClient
from flask_graphite import FlaskGraphite
import os, redis

class Service(object):
    def __init__(self):
        self.application = Flask(__name__)
        
        metric_sender = FlaskGraphite()
        self.application.config["FLASK_GRAPHITE_HOST"] = "graphite"
        self.application.config["FLASK_GRAPHITE_PORT"] = 8080
        metric_sender.init_app(self.application)
        
        self.database = MongoClient(
            os.environ["MONGO_URI"],
            username=os.environ["MONGO_USERNAME"],
            password=os.environ["MONGO_PASSWORD"]
        )
        self.cache = redis.StrictRedis(
            host=os.environ["REDIS_HOST"], 
            port=os.environ["REDIS_PORT"],
            decode_responses=True
        )

service = Service()