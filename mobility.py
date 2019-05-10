from flask import Flask, jsonify
import clients

app = Flask(__name__)

@app.route("/")
def greet_user():
   return "Ciao!"

@app.route("/<region>/all")
def all_bike_data(region):
   try:
      res = {}
      for client in clients.get_all():
         res[client.NAME] = client.all_bikes(region)
         
      return jsonify(res)
   except Exception as e:
      return jsonify({"error":str(e)})


################################################################################
# For running app at command line.

if __name__ == "__main__":

    app.run(host="0.0.0.0")