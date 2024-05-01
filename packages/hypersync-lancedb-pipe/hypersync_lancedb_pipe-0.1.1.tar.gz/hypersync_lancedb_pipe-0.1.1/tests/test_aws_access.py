import boto3
from botocore.exceptions import NoCredentialsError

# Initialize a session using IAM role or environmental credentials
session = boto3.Session(
    region_name='us-west-2'
)

# Create an S3 client
s3_client = session.client('s3')

# Use the Access Point ARN to put or get objects
bucket_arn = 'arn:aws:s3:us-west-2:560961124665:accesspoint/pipeline'

try:
    # Example: Upload a file
    response = s3_client.upload_file(
        'localfile.txt', bucket_arn, 'your-file-key')
except FileNotFoundError:
    print("The file was not found")
except NoCredentialsError:
    print("Credentials not available")
