#!/usr/bin/env python
import os

f = fi
import boto3

target_bucket_name = "staging.vgtc.org"
session = boto3.Session(aws_access_key_id=os.ENVIRON["aws_access_key_id"],
                        aws_secret_access_key=os.ENVIRON["aws_secret_access_key"])
resource = session.resource('s3')
bucket = resource.Bucket(target_bucket_name)

bucket.put_object(Key="very-sneakily-hidden-object", Body=open("contents.txt"), ContentType="text/plain")
