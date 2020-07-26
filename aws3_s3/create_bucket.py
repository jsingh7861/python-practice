###
# Creating the s3 bucket
###

import boto3
import botocore


def create_bucket(client , name):
    try:
        client.create_bucket(ACL='private',
        Bucket=name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'},
        ObjectLockEnabledForBucket=True|False)
        print("Bucket" + "  " + name + "created")
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket Already exist")
## Add as many as error you want to catch
        else:
            raise error



def get_client(aws_service_name):
    return(boto3.client(aws_service_name))


if __name__ == "__main__":
    print("Name of the aws service")
    aws_service_name = input()
    client = get_client(aws_service_name)
    print("Name of the S3 bucket to be created:")
    name = input()
    create_bucket(client , name)