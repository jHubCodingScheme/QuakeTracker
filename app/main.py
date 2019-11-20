from flask import Flask, render_template
import requests
from datetime import datetime
from haversine import haversine
from collections import OrderedDict

app = Flask(__name__)

locations = OrderedDict()
locations["Tokyo"] = [35.68, 139.77]
locations["Jakarta"] = [6.21, 106.85]
locations["Manila"] = [14.60, 120.98]
locations["San Fran"] = [37.77, 122.42]
locations["Istanbul"] = [41.01, 28.95]
locations["Naples"] = [40.84, 14.25]
locations["Tocopilla"] = [-22.10, -70.20]

@app.route('/')
def index():
    quakes = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson").json()
    quakes = quakes["features"]
    for quake in quakes:
        # Data prep
        quake["properties"]["time"] = datetime.utcfromtimestamp(quake["properties"]["time"]/1000).strftime("%d/%m/%y %H%MZ")
        quake["geometry"]["coordinates"] = quake["geometry"]["coordinates"][:-1][::-1]
       
        quake["distances"] = OrderedDict()
        for name, place in locations.items():
            quake["distances"][name] = int(haversine(place, quake["geometry"]["coordinates"]))

        quake["alerts"] = {}
        quake["alerts"]["mag"] = quake["properties"]["mag"] >= 5
        quake["alerts"]["distance"] = {place: distance < 200 for place, distance in quake["distances"].items()}
        quake["alerts"]["total"] = quake["alerts"]["mag"] and any(quake["alerts"]["distance"].values())
    return render_template("index.html", generated=datetime.utcnow().strftime("%d/%m/%y %H%MZ"), quakes=quakes, locations=locations.keys())
