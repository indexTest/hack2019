#!/usr/bin/env python
 
from flask import Flask, json, request
import pymysql

# Open database connection
db = pymysql.connect("aliasMeToDB","viper","viper67","IXPlus")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
#db.close()

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/addsegment', methods=['GET'])
def addSegment():
	segment = request.args.get('segment')
	pid     = request.args.get('pid')
	

if __name__ == '__main__':
	api.run()
