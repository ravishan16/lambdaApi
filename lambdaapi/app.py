from chalice import Chalice
import boto3,json,os

app = Chalice(app_name='lambdaapi')

S3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = os.getenv('BUCKET_NAME')

@app.route('/echo/{name}')
def echo(name):
    request = app.current_request
    S3.put_object(Bucket=BUCKET_NAME, Key=name,
                  Body=json.dumps(request.json_body))
    return {'hello': name}
