from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mission")
def mission():
    return render_template('mission.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

if __name__ == "__main__":
    app.run(debug=True)
