import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    print("Airbnb Events GOT for Putting into S3 Bucket: ",event)
    
    resp = event[0]
    bookings_order_list = eval(resp['body'])
    
    # Convert the list of dictionaries to a JSON string
    json_data = json.dumps(bookings_order_list)
    
    # Generate the filename based on the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
    file_key = f'bookings_data_{timestamp}.json'
    
    # Specify the S3 bucket name
    bucket_name = 'airbnb-booking-records-na'
    
    # Upload the JSON file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_key,
        Body=json_data
    )
    
    print('Successfully written the Airbnb Bookings data into S3 Bucket')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Airbnb bookings data JSON file uploaded to S3 with filename: {file_key}')
    }