from flask import Flask
from flask_cors import CORS
#import ab
import re
import socket
from sys import exit
import random
import json
import csv


#the constructor
app = Flask(__name__)
#app = ab.ab(str(raw_input("Enter name of book  (Will be created if doesn't exist) \n> ")))
#main_menu = '\n1. Show all contacts.\n2. Add contact.\n3. Search.\n4. Delete a contact.\n5.Update contact.\n6. Exit\n\n>'

with open('address_file.txt', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print(row)
@app.route('/')
def hello():
    with open('address_file.txt', newline='') as myFile:
        reader = csv.reader(myFile)
        l = []
        for row in reader:
            r = {}
            r['first_name'] = row[0]
            r['last_name'] = row[1]
            l.append(r)
        return json.dumps(l)


if __name__=='__main__':
   app.run(host=socket.gethostname(),port=5254)
