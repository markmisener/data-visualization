from flask import Flask, render_template
import os

app = Flask(__name__)

# set Mapbox access token
token = os.getenv('MAPBOX_ACCESS_TOKEN')

@app.route('/')
def hello():
    return render_template('us-population-density.html', MAPBOX_ACCESS_TOKEN=token)

if __name__ == '__main__':
    app.run()
