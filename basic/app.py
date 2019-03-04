# flask_web/app.py
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    # cd basic
    # docker build -t basic .
    # docker run -i -t -p 5000:5000 basic:latest
    app.run(host='0.0.0.0', port=5000, debug=True)
