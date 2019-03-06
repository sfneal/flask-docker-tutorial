from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello there, we have deployed our Flask app Docker container to AWS!'


if __name__ == '__main__':
    # cd basic
    # docker build -t basic .
    # docker run -i -t -p 5000:5000 basic:latest
    app.run(host='0.0.0.0', port=5000, debug=True)
