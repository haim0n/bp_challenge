from collections import defaultdict


def parse_data(sum_results, data_item):
    """Observer's parse function

    :param sum_results: cumulative results placeholder
    :param data_item: new data to parse and store
    :return: summary of the parsed data with sum results
    """
    event_type = data_item.get('event_type', None)
    if event_type:
        res_events = sum_results['events']
        res_events[event_type] = res_events.get(event_type, 0) + 1

    data = data_item.get('data', None)
    if data:
        res_data = sum_results['data']
        for word in data.split():
            res_data[word] = res_data.get(word, 0) + 1
    return sum_results


def create_results():
    return {'events': defaultdict(int),
            'data': defaultdict(int)}
