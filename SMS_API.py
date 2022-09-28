# importing libraires
from twilio.rest import Client

# tokens
sid='AC07869bffb1c2f3394eac9438f7db6320'
authToken='9f73c82bfb8905e213e8dd0f3f178014'

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