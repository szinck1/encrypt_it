from flask import Flask


app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def hello() -> str:
    return "Hello, World"
