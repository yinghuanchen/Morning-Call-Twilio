from twilio.rest import Client
import yaml
import schedule 

with open("credentials.yaml") as f:  
  creds = yaml.safe_load(f)

client = Client(creds['account'], creds['token'])
message = client.messages.create(to="+13108908971", from_="+16263228841",
                                 body="Happy Birthday!")
print(message.sid)
