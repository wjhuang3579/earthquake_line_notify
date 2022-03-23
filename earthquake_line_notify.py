#!/usr/bin/env python3
import params
import requests
import argparse
import time

from params import TOKEN

parser = argparse.ArgumentParser()
parser.add_argument("level")
parser.add_argument("seconds")
args = parser.parse_args()

earthquake_level = args.level
earthquake_seconds = args.seconds
t_future = time.time() + float(earthquake_seconds)

message = '震度 ' + earthquake_level + ' 級，將於 ' + \
    time.strftime("%I 點 %M 分", time.localtime(t_future)) + ' 抵達。'


def lineNotifyMessage(_token, _msg):

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-Type": "application/form-data"
    }

    payload = {
        'message': _msg
    }

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers,
                      params=payload
                      )
    return r.status_code


if __name__ == "__main__":
    __token__ = TOKEN
    lineNotifyMessage(__token__, message)
