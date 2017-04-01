# lambdaApi
Boilerplate for AWS Lambda api using chalice

## Simple Python App using Chalice and Boto

- Exposes a new endpoint /echo/{name}
- Response Json prints out name
- Picks up the s3 bucket and region from lambda environment variable
- Logs the request in s3
- Debuging enables logs can be viewed in cloud watch
- Chalice deploy used to deploy the lambda fuction
