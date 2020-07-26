###
# Program to set the bucket encryption 
###

import boto3



def put_encryption(bucket_name , client):
    set_encryption = client.put_bucket_encryption(Bucket = bucket_name,  
    ServerSideEncryptionConfiguration = { 
        'Rules' : [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256',
                    }
            },
        ]
    }
    
)

def get_client(aws_service_name):
    return(boto3.client(aws_service_name))


if __name__ == "__main__":
    print("Enter the aws service name :")
    aws_service_name = input()
    client = get_client(aws_service_name)
    print("Enter the Bucket name to find the encryption :")
    bucket_name = input()
    put_encryption(bucket_name , client)
    