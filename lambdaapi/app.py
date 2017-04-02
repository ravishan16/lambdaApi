#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chalice App."""
import datetime
import json
import logging
import os

import boto3
from chalice import Chalice

APP = Chalice(app_name='lambdaapi')
APP.log.setLevel(logging.DEBUG)
S3 = boto3.client('s3', region_name=os.getenv('REGION_NAME'))
BUCKET_NAME = os.getenv('BUCKET_NAME')


def log_request_s3(name):
    """Function to Log request in s3."""
    try:
        request = APP.current_request
        S3.put_object(Bucket=BUCKET_NAME,
                      Key=name + '_' + str(datetime.datetime.now()),
                      Body=json.dumps(request.to_dict()))
    except Exception as e:
        APP.log.error("Logging the request in S3 Failed %s", e)


@APP.route('/echo/{name}')
def echo_name(name):
    """echo End Point take name and returns name as json."""
    APP.log.debug("Calling /echo/%s", name)
    log_request_s3(name)
    return {'hello': name}
