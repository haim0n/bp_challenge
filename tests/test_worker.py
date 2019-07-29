from bp_challenge import worker

DUMMY_DATA = (
    {"event_type": "foo", "data": "lorem", "timestamp": 1564501799},
    {"event_type": "baz", "data": "ipsum", "timestamp": 1564501799},
    {"event_type": "foo", "data": "dolor", "timestamp": 1564501799},
    {"event_type": "foo", "data": "lorem", "timestamp": 1564501799},
    {"event_type": "foo", "data": "ipsum", "timestamp": 1564501802},
    {"event_type": "bar", "data": "lorem", "timestamp": 1564501802},
    {"event_type": "bar", "data": "dolor", "timestamp": 1564501802},
    {"event_type": "bar", "data": "sit", "timestamp": 1564501802},
    {"event_type": "bar", "data": "lorem", "timestamp": 1564501802},
    {"event_type": "bar", "data": "lorem", "timestamp": 1564501802},
    {"event_type": "baz", "data": "dolor", "timestamp": 1564501802},
    {"event_type": "bar", "data": "ipsum", "timestamp": 1564501802},
    {"event_type": "bar", "data": "sit", "timestamp": 1564501804},
    {"event_type": "bar", "data": "sit", "timestamp": 1564501804},
    {"event_type": "baz", "data": "dolor", "timestamp": 1564501804},
    {"event_type": "foo", "data": "dolor", "timestamp": 1564501804},
    {"event_type": "bar", "data": "sit", "timestamp": 1564501808},
    {"event_type": "baz", "data": "lorem", "timestamp": 1564501808},
    {"event_type": "foo", "data": "tree dolor", "timestamp": 1564501808},
    {"event_type": "bar", "data": "dolor sitting tree",
     "timestamp": 1564501808},
)


def test_parse_data_event_count():
    results = worker.create_results()
    for d in DUMMY_DATA:
        results = worker.parse_data(results, d)

    expected = {'foo': 6, 'baz': 4, 'bar': 10}
    for e, v in expected.items():
        assert v == results['events'][e]


def test_parse_data_word_count():
    results = worker.create_results()
    for d in DUMMY_DATA:
        results = worker.parse_data(results, d)

    expected = {'lorem': 6, 'ipsum': 3, 'dolor': 7, 'sit': 4, 'tree': 2,
                'sitting': 1}
    for w, v in expected.items():
        assert v == results['data'][w]
