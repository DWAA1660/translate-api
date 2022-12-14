from flask import Flask
from translate import Translate

app = Flask(__name__)
translate = Translate(geckodriver_path="/home/david/Documents/GitHub/translate-api/geckodriver")

@app.route('/api/')
def index():
    return({'Welcome': 'Welcome to translate Api'})

@app.route('/api/to_spanish/<text>')
def to_spanish(text):
    return({'translation': translate.to_spanish(text)})

@app.route('/api/to_french/<text>')
def to_french(text):
    return({'translation': translate.to_french(text)})

if __name__ == '__main__':
    app.run(debug=True)