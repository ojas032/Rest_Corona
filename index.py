from flask import Flask,jsonify
from flask_restful import Resource, Api
import requests 
from bs4 import BeautifulSoup 

app = Flask(__name__)
api = Api(app)


class GET(Resource):
    def get(self):
        URL = "https://www.worldometers.info/coronavirus/country/india/"
        r = requests.get(URL) 

        soup = BeautifulSoup(r.content, 'html5lib')

        detail=[] 

        detail=soup.findAll("div",{"class":"maincounter-number"})

        print(len(detail))

        dict={}

        for ind,i in enumerate(detail):
            #print(ind,i.span.text)
            dict[ind]=i.span.text
        print(dict)
        return jsonify(dict)
       

api.add_resource(GET,"/get")        

#print(soup.prettify()) 

if __name__ == '__main__':
     app.run(debug=True)