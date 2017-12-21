#!/bin/bash
sudo apt-get install python
virtualenv venv
. ./venv/bin/activate
pip install boto3

mkdir ~/.aws
echo "[default]" > ~/.aws/credentials
echo "aws_access_key_id = $aws_access_key_id" >> ~/.aws/credentials
echo "aws_secret_access_key = $aws_secret_access_key" >> ~/.aws/credentials


