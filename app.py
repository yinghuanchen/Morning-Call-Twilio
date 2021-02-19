from twilio.rest import Client
import yaml
import schedule 

with open("credentials.yaml") as f:  
  creds = yaml.safe_load(f)

client = Client(creds['account'], creds['token'])

def job():
    call = client.calls.create(to="+13108908971",
                               from_="+16263228841",
                             url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

schedule.every().day.at("8:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

