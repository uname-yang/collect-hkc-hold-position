#!/usr/bin/env python3

import logging
import time
import os
import json
import redis

# # Kafka Configurations
# KAFKA_HOST_NAME = os.environ.get('KAFKA_HOST_NAME')
# KAFKA_TOPIC_NAME = os.environ.get('KAFKA_TOPIC_NAME')

def main():
    logging.info("Start Point.")
    

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
