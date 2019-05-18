import re
import socket
from sys import exit
import random
import json
import csv
import pandas as pd

#the constructor
app = Flask(__name__)

@app.route('/')       
def hello(): 
    return 'HELLO: Welcome to Address Book Application'

@app.route('/load_data')
def load_data():
        global df
        with open('address_file.txt', newline='') as myFile:
                reader = csv.reader(myFile)
                l = []
                for row in reader:
                    r = {}
                    r['first_name'] = row[0].lower()
                    r['last_name'] = row[1].lower()
                    r['street_add'] = row[2].lower()
                    r['city'] = row[3].lower()
                    r['state'] = row[4].lower()
                    r['area_code'] = row[5].lower()
                    l.append(r)

        df = pd.DataFrame(l)

        return json.dumps(l)

# ?key=first_name,value=nitish
@app.route('/query')
def query_data():
        key = request.args['key'].lower()
        value = request.args['value'].lower()
        if key not in df:
            return("Invalid Key in your query")

        new_df = df.loc[df[key] == value]
        s = new_df.to_csv(header=True, index=False, line_terminator='<br>',columns=['first_name', 'last_name', 'street_add', 'city', 'state', 'area_code'])
        if(len(new_df)>0):
            return s.replace(',', '&#44;')
        else:
            return("Data is not present in the Address Book")
        #return len(new_df)
        #return s
        #abort(make_response(s), 200)

if __name__=='__main__':
   app.run(host=socket.gethostname(),port=5254)
