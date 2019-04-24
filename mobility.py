import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
   return "Ciao!"

class BaseBikeClass:
   NAME = ''
   BASE_URL = ''
   METADATA = {}

class Jump(BaseBikeClass):
   def __init__(self):
      self.NAME = 'jumpbikes'
      self.BASE_URL = 'jumpbikes.com/opendata'
      self.METADATA = {}

   def allBikes(self, region):
      if region not in ['atx', 'nyc', 'chi', 'sc', 'dc', 'san', 'sac', 'pvd', 'mia']:
         return "There are no bikes in {0}".format(region)
      url = "https://{0}.{1}/free_bike_status.json".format(region, self.BASE_URL)
      r = requests.get(url)
      data = r.json()
      return data

Clients = [Jump()]
@app.route("/<region>/all")
def all_bikes(region):
   return jsonify({client.NAME:client.allBikes(region) for client in Clients})