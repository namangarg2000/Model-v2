import Face_recog12 as fr
from unicodedata import name
from flask import Flask, jsonify
app = Flask(__name__)

def recog():
    print("Calling recognition function")


fr.recog()

@app.route('/')
def hello_world():
    recog()
    return jsonify({"N":2})

if __name__ == '__main__':
    app.run(host="0.0.0.0")