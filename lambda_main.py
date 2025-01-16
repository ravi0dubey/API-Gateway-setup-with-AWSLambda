from fastapi import FastAPI,File,Form, UploadFile
from mangum import Mangum 
import os
from datetime import datetime
from upload_pdf_to_s3 import upload_image_from_memory_to_s3_boto3,read_yaml_file

lambdamainapi = FastAPI()
handler = Mangum(lambdamainapi)


@lambdamainapi.get("/")
async def root():
    return {"message": "Welcome to the LambdaMain userdocument_upload API"}


@lambdamainapi.post('/userdocument_upload')
async def document_upload(file: UploadFile = File(...), user_id: str = Form(...)):
    print("inside userdocument_function")
    env_file_path=os.path.join(os.getcwd(),"env.yaml")
    env_return=read_yaml_file(env_file_path)
    s3_bucket= env_return['BUCKET_NAME']
    userdocument_image_content = file.file.read()
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m-%d-%Y")
    userdocument_image_key =f"{user_id}/{user_id}_userdocument_{formatted_date}.jpg"
    upload_report_response = upload_image_from_memory_to_s3_boto3(s3_bucket,userdocument_image_content,userdocument_image_key,user_id)
    return upload_report_response



if __name__ == "__main__":
    print("inside _name_")
    from uvicorn import run as lambdamain_run
    lambdamain_run(lambdamainapi, host="127.0.0.1", port=8005)