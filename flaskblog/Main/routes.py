from flask import  render_template, Blueprint, Flask
from flask_googlemaps import GoogleMaps, Map
from flaskblog import app

inicial = Blueprint('inicial', __name__ )

'''
with open('.env') as f:
    api_key = f.readline()
    api_key = api_key.rstrip('\n')
    f.close()
'''
api_key = "AIzaSyCsZtbvEO_tPJiX8cND6_P7wEdhkL_Af7o"

@inicial.route("/" )

def createMap():


    mymap = Map(
        identifier="sndmap",

        style=(
            "height:75%;"
            "width:50%;"
            "top:100px;"
            "left:550px;"
            "position:absolute;"
            "zIndex:999;"
        ),
        lat=-22.978993,
        lng=-43.233160,
        markers=,
        zoom="16"
    )
    return mymap
def home():
    GoogleMaps(app, key=api_key)
    mymap = createMap()
    return render_template('home.html', title = "Imoveis Estudantis",  mymap=mymap )

@inicial.route("/about")
def about():
    return render_template('about.html')