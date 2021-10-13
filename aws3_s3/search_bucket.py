###
# Searching the specific bucket from s3
###


import boto3



def search_bucket(client , bucket_name):
    s3_bucket = client.list_buckets()
    buckets = s3_bucket.get('Buckets')
    search = False
    for name in buckets:
        name_var = name.get('Name')
        if name_var == bucket_name:
            search = True
            print("Bucket found", bucket_name)
            break
    else:
        print("Bucket not found")            

def get_client(aws_service_name):
    return(boto3.client(aws_service_name))
    

if __name__ == "__main__":
    print("Enter the AWS service name:")
    aws_service_name = input()
    client = get_client(aws_service_name)
    print("Enter the name of the Bucket to be searched")
    bucket_name = input()
    search_bucket(client, bucket_name)
   

