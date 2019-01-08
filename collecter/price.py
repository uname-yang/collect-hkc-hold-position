#!/usr/bin/env python3

import logging
import time
import os
import json
import redis
import pysnowball as ball


def main():
    logging.info("Start Point.")
    db = redis.Redis(host='redis', port=6379, db=0)

    codes_sz = db.get('CODES:SZ')
    codes_sh = db.get('CODES:SH')

    if codes_sz == None or codes_sh == None:
        return 
    codes_sz = codes_sz.decode("utf-8")
    codes_sh = codes_sh.decode("utf-8")

    # logging.info(codes_str)
    codes_str = codes_sz+"|"+codes_sh
    codes = codes_str.split("|")

    for code in codes:
        acode = tran_code(code)
        name = db.get('NAME:'+code).decode("utf-8")
        hold = int(db.get('HOLD:'+code).decode("utf-8"))

        price = quote(acode)
        capital = price * hold

        obj = {
            'acode': acode,
            'code': code,
            'name': name,
            'hold': hold,
            'price': price,
            'capital': capital,
        }

        db.set('VIEW:'+code, json.dumps(obj))

    logging.info("End Point.")


#| from | 70 | 71 | 72  | 77  | 90  | 93  |
#| to | 000 | 001 | 002 | 300 | 600 | 603 |

def tran_code(code):
    code_str = str(code)
    d2 = code_str[0:2]
    d3 = code_str[2:5]

    if d2 == "70":
        return 'SZ000'+d3
    elif d2 == "71":
        return 'SZ001'+d3
    elif d2 == "72":
        return 'SZ002'+d3
    elif d2 == "77":
        return 'SZ300'+d3
    elif d2 == "90":
        return 'SH600'+d3
    elif d2 == "91":
        return 'SH601'+d3
    elif d2 == "92":
        return 'SH602'+d3
    elif d2 == "93":
        return 'SH603'+d3
    else:
        logging.error(code_str)
        raise('tran_code error:'+code_str)


def quote(code):
    # logging.info(code)
    data = ball.quotec(code)
    # logging.info(data)
    return data['data'][0]['current']


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
