import datetime
import random as rd
import pprint


def generate_time_series(*args, **kwargs):
    timeseries = []
    for key, length in kwargs.items():
        series = {
            'name': key,
            'data': []
        }
        const_delta = datetime.timedelta(0, rd.randint(1, 10))
        for i in range(length):
            str_time = str((datetime.datetime.now() + datetime.timedelta(0, i) + const_delta).replace(microsecond=0))
            series['data'].append([str_time, rd.randint(10, 100)])
        timeseries.append(series)
    return timeseries

pprint.pprint(generate_time_series(http_201=10,http_202=12,http_404=5))