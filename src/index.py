from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/DC2/")
def DC2():
  return render_template('DC2.html')

@app.route("/DC5/")
def DC5():
  return render_template('DC5.html')

@app.route("/Supra/")
def Supra():
  return render_template('Supra.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)







