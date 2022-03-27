import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAZ4ZV2KF4FYI7GLSY'
SECRET_KEY = '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'


def upload_to_aws(doc.jpg, mrappbucks, doc.jpg):
    s3 = boto3.client('s3', aws_access_key_id='AKIAZ4ZV2KF4FYI7GLSY',
                      aws_secret_access_key='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')

    try:
        s3.upload_file(doc.jpg, mrappbucks, doc.jpg)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('doc.jpg', 'mrappbucks', 'doc.jpg')
