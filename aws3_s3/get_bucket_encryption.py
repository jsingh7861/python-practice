###
# Program to find the bucket encryption 
###

import boto3


def get_encryption(bucket_name , client):
    response = client.get_bucket_encryption(Bucket = bucket_name)
    print(response)



def get_client(aws_service_name):
    return(boto3.client(aws_service_name))


if __name__ == "__main__":
    print("Enter the aws service name :")
    aws_service_name = input()
    client = get_client(aws_service_name)
    print("Enter the Bucket name to find the encryption :")
    bucket_name = input()
    get_encryption(bucket_name , client)