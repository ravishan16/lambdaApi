#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import datetime
import json
import logging
import os
from chalice import Chalice

app = Chalice(app_name='lambdaapi')
app.log.setLevel(logging.DEBUG)

S3 = boto3.client('s3', region_name=os.getenv('REGION_NAME'))
BUCKET_NAME = os.getenv('BUCKET_NAME')



"""
echo End Point take name and returns name as json
"""
@app.route('/echo/{name}')
def echo(name):
    app.log.debug("Calling /echo/%s", name)
    request = app.current_request

    S3.put_object(Bucket=BUCKET_NAME, Key=name + '_' + str(datetime.datetime.now()),
                  Body=json.dumps(request.to_dict()))
    return {'hello': name}

"""
    Function to Count
"""
def count():
    return 1
