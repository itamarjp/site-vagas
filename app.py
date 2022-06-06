from flask import Flask, render_template
import pymongo

app = Flask(__name__)


url = ""
dbName = ""
collectionName =""

#myclient = pymongo.MongoClient(url)
#mydb = myclient[dbName]
#mycol = mydb[collectionName]


@app.route("/")
def hello_world():
    return render_template("index.html")
