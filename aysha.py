from twilio.rest import Client
from geopy.distance import geodesic

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create Twilio client
client = Client(account_sid, auth_token)

# Ambulance current GPS coordinates (example)
ambulance_location = (40.748817, -73.985428)  # Example: coordinates of the ambulance

# List of recipients with their GPS coordinates
recipients = [
    {"phone": "+1234567890", "location": (40.748000, -73.986000)},  # Close to ambulance
    {"phone": "+1987654321", "location": (40.730610, -73.935242)},  # Farther away
]

# Define the radius (in kilometers) for sending SMS
radius = 2  # 2 km radius

# Loop through recipients and send SMS if within radius
for recipient in recipients:
    distance = geodesic(ambulance_location, recipient["location"]).km
    if distance <= radius:
        message = client.messages.create(
            body="🚨 Ambulance Alert: An ambulance is en route to [destination] via [Route Name]. Please clear the way for emergency services.",
            from_='+1234567890',  # Your Twilio number
            to=recipient["phone"]
        )
        print(f"Sent message to {recipient['phone']} - Distance: {distance} km")
