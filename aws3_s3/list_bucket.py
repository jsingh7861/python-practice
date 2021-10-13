###
# Python program to list the S3 bucket names
###

import boto3



def list_bucket(client):
    s3_bucket = client.list_buckets()
    buckets = s3_bucket.get('Buckets')
    for name in buckets:
        print(name.get('Name'))

def get_client(aws_service_name):
    return(boto3.client(aws_service_name))
    

if __name__ == "__main__":
    print("Enter the AWS service name:")
    aws_service_name = input()
    client = get_client(aws_service_name)
    list_bucket(client)
   
 



