# importing libraires
from twilio.rest import Client

# tokens
sid='AC07869bffb1c2f3394eac9438f7db6320'
authToken='64d9cfcc65f6c58f3fb95a2534f9dfbd'

client = Client(sid, authToken)

# info
from_number='whatsapp:+14155238886'
message='Hi this is a BOT Message'
to_number='whatsapp:+918553829986' 

message = client.messages.create(
    from_=from_number,
    body=message,
    to=to_number
) 
print(message.sid)