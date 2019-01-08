#!/usr/bin/env python3

import logging
import time
import os
import json
import redis
import pyhkconnect as hkc

# # Kafka Configurations
# KAFKA_HOST_NAME = os.environ.get('KAFKA_HOST_NAME')
# KAFKA_TOPIC_NAME = os.environ.get('KAFKA_TOPIC_NAME')


def main():
    logging.info("Start Point.")
    db = redis.Redis(host='redis', port=6379, db=0)

    sh = hkc.northbound_shareholding_sh()
    json_obj = sh.to_json(orient='index')
    

    # sz = hkc.northbound_shareholding_sz()

    logging.info("End Point.")


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
