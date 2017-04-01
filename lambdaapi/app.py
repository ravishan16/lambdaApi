#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chalice import Chalice
import boto3,json,os,logging,datetime

app = Chalice(app_name='lambdaapi')
app.log.setLevel(logging.DEBUG)

S3 = boto3.client('s3', region_name=os.getenv('REGION_NAME'))
BUCKET_NAME = os.getenv('BUCKET_NAME')

@app.route('/echo/{name}')
def echo(name):
    app.log.debug("Calling /echo/%s",name)
    request = app.current_request

    S3.put_object(Bucket=BUCKET_NAME, Key=name+'_'+str(datetime.datetime.now()),
                  Body=json.dumps(request.to_dict()))
    return {'hello': name}


def count():
    return 1
