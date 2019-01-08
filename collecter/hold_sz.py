#!/usr/bin/env python3

import logging
import time
import os
import json
import redis
import pyhkconnect as hkc


def main():
    logging.info("Start Point.")
    db = redis.Redis(host='redis', port=6379, db=0)

    sz = hkc.northbound_shareholding_sz()
    json_str = sz.to_json(orient='values')
    json_obj = json.loads(json_str)

    for record in json_obj:
        code = record[0]
        name = record[1]
        held = int(record[2].replace(',', ''))

        logging.info("set:" + json.dumps(record))

        db.set('HOLD:'+code, held)
        db.set('NAME:'+code, name)

    logging.info("End Point.")


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
