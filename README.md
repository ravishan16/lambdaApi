
# Simple API using Chalice to build and deploy Lambda function

[![Build Status](https://travis-ci.org/ravishan16/lambdaApi.svg?branch=feature)](https://travis-ci.org/ravishan16/lambdaApi)
[![Code Climate](https://codeclimate.com/github/ravishan16/lambdaApi/badges/gpa.svg)](https://codeclimate.com/github/ravishan16/lambdaApi)

lambdaApi- Boilerplate for building and deploying AWS Lambda function using chalice

## Simple Python App using Chalice and Boto

- Exposes a new endpoint /echo/{name}
- Response Json prints out name
- Picks up the s3 bucket and region from lambda environment variable
- Logs the request in s3 (boto3)
- Debuging enables logs can be viewed in cloud watch
- Chalice deploy used to deploy the lambda function
- travis-ci to build, run test
- code climate for static code analysis and test coverage report
  [Code Climate Docs](https://docs.codeclimate.com/v1.0/)
  [Code Climate pull-requests setup](https://docs.codeclimate.com/v1.0/docs/github#pull-requests)

### Clone and Install requirements

```python
  git clone git@github.com:ravishan16/lambdaApi.git
  pip install -r requirements.txt
```

### AWS Cli configure

- [AWS CLI CONFIGURE](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-command-line)

```python
  awscli configure
```

### Deploy code to AWS

```python
  cd lambdaApi/lambdaapi
  chalice deploy
```

## License

[MIT](https://github.com/atom/atom/blob/master/LICENSE.md)
