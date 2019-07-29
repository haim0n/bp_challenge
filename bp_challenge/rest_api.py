import flask
from flask import Flask

app = Flask(__name__)

results = {}


@app.route('/events/countByEventType')
def get_events_count_by_type():
    return flask.jsonify('results')


@app.route('/events/countWords')
def get_events_count_words():
    return "Hello2"


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
