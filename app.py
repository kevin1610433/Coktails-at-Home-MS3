import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
@app.route("/get_cocktails")
def get_cocktails():
    cocktails = mongo.db.cocktails.find()
    return render_template("cocktails.html", cocktails=cocktails)

@app.route("/")
def cocktails():
    return "Cocktails at Home!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)