"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq2e9mbg5e4khq7lgg-a.oregon-postgres.render.com",
        database="todo_oltd",
        user="root",
        password="OBiKFM7TQn9cynypqCNp407Gk750tk90")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
