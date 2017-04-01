from setuptools import setup

setup(
    name='lambdaapi',
    version='0.0.1',
    url='https://github.com/ravishan16/lambdaapi',
    license='MIT',
    author='Ravishankar Sivasubramaniam',
    author_email='ravi_siva@live.com',
    description='Lambda API Boiler Plate',
    packages=['lambdaapi'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'boto3',
        'chalice',
        'awscli',
        'pylint',
        'nose'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
