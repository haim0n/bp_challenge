#!/usr/bin/env python
import functools
import threading

import flask
import rx
from rx import operators as op
from flask import Flask

import producer
import worker

app = Flask(__name__)

results = {}


@app.route('/events/countByEventType')
def get_events_count_by_type():
    return flask.jsonify(results.get('events'))


@app.route('/events/countWords')
def get_events_count_words():
    return flask.jsonify(results.get('data'))


def update_results(val):
    global results
    results = val


def start_rest_api():
    rest_api = threading.Thread(target=app.run, kwargs={'port': 8080})
    rest_api.start()


def main():
    start_rest_api()
    res = worker.create_results()
    source = rx.from_iterable(producer.generate_data())
    source.pipe(
        op.map(functools.partial(worker.parse_data, res)),
    ).subscribe(update_results)


if __name__ == '__main__':
    main()
