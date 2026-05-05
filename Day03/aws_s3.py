import boto3

s3 = boto3.resource('s3')

def show_all_buckets():
    for bucket in s3.buckets.all():
        print('hello')
        print(bucket.name)
        

def upload_to_bucket(s3,file_name,bucket_name,source_path):
    
    data = open(source_path,'rb')
    s3.Bucket(bucket_name).put_object(key=file_name,Body=data)
    print("Backup stored to s3")
    
    source_path = "Users/navinsinghhajari/backups/backup2026-05-05.tar.gz"
    bucket_name = "navindevops"
    file_name = "backup2026-05-05.tar.gz"
    
    upload_to_bucket(s3,file_name,bucket_name,source_path)

    

