import yaml
import boto3
from botocore.exceptions import BotoCoreError, ClientError


def read_yaml_file(file_path: str) -> dict:
    """   
    Input values  :
       a. File path where .yaml exists
    Function: 
    a. It reads the .yaml file and return the content in form of dict.
    """ 
    try:
        print(f"inside run read_yaml_file filepath  :  {file_path} ")
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        return {"status": "error", "result": f"Error reading  env.yaml_file: {e}"}


        
def upload_image_from_memory_to_s3_boto3(bucket_name, image_data, image_key, user_id):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=bucket_name, Key=image_key, Body=image_data)
        return {"status": "success", "result": f"Document successfully uploaded for {user_id}."}
    except (BotoCoreError, ClientError) as e:
        return {"status": "error", "result": f"Error in uploading document to S3: {e}"}