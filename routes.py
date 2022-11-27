from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')



if __name__ == "__main__":
  # If you are debugging you can do that in the browser:
  app.run(debug=True)
  # If you want to view the flaskwebgui window:
#   FlaskUI(app=app, server="flask").run()