from flask import Flask, render_template, request, redirect, url_for, abort
from flask_googlemaps import GoogleMaps
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyD8lo57FQDuV0Y9c_RcjjxUrJIfXFb-3O0"

GoogleMaps(app)

GoogleMaps(app, key="AIzaSyD8lo57FQDuV0Y9c_RcjjxUrJIfXFb-3O0")

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/DC2/")
def DC2():
  return render_template('DC2.html')

@app.route("/DC5")
def DC5():
  return render_template('DC5.html')

@app.route("/Supra/")
def Supra():
  return render_template('Supra.html')

@app.route("/S13/")
def S13():
  return render_template('S13.html')

@app.route("/S15/")
def S15():
  return render_template('S15.html')

@app.route("/Chaser/")
def Chaser():
  return render_template('Chaser.html')

@app.route("/Map/")
def Map():
  return render_template('Map.html')

@app.errorhandler(404)
def page_not_found (error):
  return "<strong>OOPS!!!! PAGE NOT FOUND!! PLEASE RETURN TO HOMEPAGE =]</STRONG>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)







