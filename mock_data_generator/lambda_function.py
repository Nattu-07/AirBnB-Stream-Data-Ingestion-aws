import json
import boto3
sqs_client = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/891377251081/AirbnbBookingQueue'

import uuid
import random
from datetime import datetime, timedelta

# Function to generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())

# Function to generate a random UserID
def generate_user_id():
    # Example: generate a random 6-digit user ID
    return ''.join(random.choices('0123456789', k=6))

# Function to generate a random PropertyID
def generate_property_id():
    # Example: generate a random 8-character property ID
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

# Function to generate a random location (City, Country)
def generate_location():
    # Example: generate a random city and country combination
    cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
    countries = ['USA', 'UK', 'France', 'Japan', 'Australia']
    city = random.choice(cities)
    country = random.choice(countries)
    return f"{city}, {country}"

# Function to generate a random date in the format YYYY-MM-DD
def generate_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

# Function to generate a random price in USD
def generate_price():
    # Example: generate a random price between $50 and $500
    return round(random.uniform(50, 500), 2)

# Generate JSON data ensuring start_date <= end_date
def generate_json_data():
    start_date = generate_date()
    end_date = generate_date()

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    booking_id = generate_uuid()
    user_id = generate_user_id()
    property_id = generate_property_id()
    location = generate_location()
    price = generate_price()

    json_data = {
        "bookingId": booking_id,
        "userId": user_id,
        "propertyId": property_id,
        "location": location,
        "startDate": start_date,
        "endDate": end_date,
        "price": price
    }
    return json_data

def lambda_handler(event, context):

    # Generate a list of N JSON data entries
    num_entries = 30
    json_data_list = [generate_json_data() for _ in range(num_entries)]
    
    # Print the generated JSON data
    for data in json_data_list:
        print(data)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(data)
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Airbnb bookings data published to SQS!')
    }
    

