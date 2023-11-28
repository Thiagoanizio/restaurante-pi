from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route('/images/<filename>')
def my_images(filename):
    return send_from_directory("images", filename)

@app.route('/css/<filename>')
def my_css(filename):
    return send_from_directory("css", filename)

@app.route('/js/<filename>')
def my_js(filename):
    return send_from_directory("js", filename)

