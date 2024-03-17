import json
from datetime import datetime

def lambda_handler(event, context):
    print("Airbnb Events GOT for Filtering: ",event)
    
    bookings_greater_than_1_day = []
    
    for cur_msg in event:
        bookings_order = json.loads(cur_msg['body'])
        start_date = datetime.strptime(bookings_order['startDate'], "%Y-%m-%d").date()
        end_date = datetime.strptime(bookings_order['endDate'], "%Y-%m-%d").date()
        date_difference = end_date - start_date
        if date_difference.days > 1:
            bookings_greater_than_1_day.append(bookings_order)
    
    print("bookings_greater_than_1_day; ",bookings_greater_than_1_day)
    
    return {
        'statusCode': 200,
        'body': json.dumps(bookings_greater_than_1_day)
    }