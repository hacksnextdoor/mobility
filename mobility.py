from flask import Flask, jsonify
import clients

app = Flask(__name__)

@app.route("/")
def hello():
   return "Ciao!"

@app.route("/<region>/all")
def all_bikes(region):
   try:
      res = {}
      for client in clients.get_all():
         res[client.NAME] = client.all_bikes(region)
      return jsonify(res)
   except Exception as e:
      return jsonify({"error":str(e)})