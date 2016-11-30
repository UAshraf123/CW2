from flask import Flask, flash, render_template, request, redirect, url_for, abort
import ConfigParser
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = 'supersecret'


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
  return render_template('404.html')

@app.route('/')
def index():
           this_route = url_for('.index')
           app.logger.info("Logging a test message from "+this_route)
           return "Configuration testing with logging"

def init(app):
           config = ConfigParser.ConfigParser()
           try:
        config_location = "etc/logging.cfg"
        config.read(config_location)
           
        app.config['DEBUG'] = config.get ("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
           
        app.config['log_file'] = config.get("logging", "name")
        app.config['log_location'] = config.get("logging", "location")
        app.config['log_level'] = config.get("logging", "level")
        except
           print "could not read configs from: ", config_location
           
def logs(app):
           log_pathname = app.config['log_location'] + app.config['log_file']
           file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10 , backupCount=1024)
           file_handler.setLevel( app.config['log_level'] )
           formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
           file_handler.setFormatter(formatter)
           app.logger.setLevel( app.config['log_level'] )
           app.logger.addHandler(file_handler)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
           init(app)
           logs(app)
           app.run(
             host=app.config['ip_address'],
             port=int(app.config['port']))







