from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "How's it going there, we have Flask in a Docker container!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
