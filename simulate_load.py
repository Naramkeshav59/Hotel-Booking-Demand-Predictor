import requests
import threading

url = "http://ecs-lb-760876054.us-east-1.elb.amazonaws.com/predict"
data = {
    "hotel": "City Hotel",
    "lead_time": 75,
    "arrival_date_month": 7,
    "arrival_date_week_number": 28,
    "arrival_date_day_of_month": 15,
    "stays_in_weekend_nights": 2,
    "stays_in_week_nights": 3,
    "adults": 2,
    "children": 1,
    "babies": 0,
    "meal": "BB",
    "market_segment": "Online TA",
    "distribution_channel": "TA/TO",
    "is_repeated_guest": 0,
    "previous_cancellations": 0,
    "previous_bookings_not_canceled": 1,
    "reserved_room_type": "A",
    "deposit_type": "No Deposit",
    "agent": 240,
    "company": 0,
    "customer_type": "Transient",
    "adr": 105.50,
    "required_car_parking_spaces": 1,
    "total_of_special_requests": 2
}

def send_request():
    for _ in range(10000):  
        requests.post(url, json=data)

threads = []
for _ in range(10):  
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Done.")
