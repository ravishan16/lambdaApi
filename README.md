# lambdaApi
[![Build Status](https://travis-ci.org/ravishan16/lambdaApi.svg?branch=feature)](https://travis-ci.org/ravishan16/lambdaApi)
[![Code Climate](https://codeclimate.com/github/ravishan16/lambdaApi/badges/gpa.svg)](https://codeclimate.com/github/ravishan16/lambdaApi)
Boilerplate for AWS Lambda api using chalice

## Simple Python App using Chalice and Boto

- Exposes a new endpoint /echo/{name}
- Response Json prints out name
- Picks up the s3 bucket and region from lambda environment variable
- Logs the request in s3
- Debuging enables logs can be viewed in cloud watch
- Chalice deploy used to deploy the lambda fuction
- Nosetests for unittest
- travis-ci to build
- code climate for static code analysis and test coverage report
  https://docs.codeclimate.com/v1.0/
  https://docs.codeclimate.com/v1.0/docs/github#pull-requests 
