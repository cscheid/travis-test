#!/usr/bin/env python
import boto3

target_bucket_name = "staging.vgtc.org"

session = boto3.Session(profile_name="default")
resource = session.resource('s3')
bucket = resource.Bucket(target_bucket_name)
bucket.put_object(Key="very-sneakily-hidden-object", Body="yup, here.", ContentType="text/plain")
