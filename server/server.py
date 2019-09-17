#!/usr/bin/env python
 
from flask import Flask, json, request

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/addsegment', methods=['GET'])
def addSegment():
	segment = request.args.get('segment')
	pid     = request.args.get('pid')
	

if __name__ == '__main__':
	api.run()
