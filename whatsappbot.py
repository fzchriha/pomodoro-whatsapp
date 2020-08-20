from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import emoji
import os 
app = Flask(__name__)


account = os.environ.get("ACCOUNT_SID")
token = os.environ.get("TOKEN")
client = Client(account, token)

# message = client.messages.create(to=user_number(), from_="whatsapp:+14155238886",
#
@app.route("/")
def Hello():
    return "Hello Team RC"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

                            
    # Fetch the message
    msg = request.form.get('Body')
    phone_number = request.form.get('From')

    #Productivity time
    msg_received = datetime.datetime.now()
    prod = msg_received + datetime.timedelta(minutes=25)
    prod_session = f"{prod.year}-{prod.month:02d}-{prod.day:02d} {prod.hour:02d}:{prod.minute:02d}:{prod.second:02d}"
    brek = msg_received + datetime.timedelta(minutes=5)
    brek_session = f"{brek.year}-{brek.month:02d}-{brek.day:02d} {brek.hour:02d}:{brek.minute:02d}:{brek.second:02d}"
    resp = MessagingResponse()      
    # Reply after session
    prod_msg = "You did a great job! Reply *Break* to take a break"
    brek_msg = "Hmm feels good to have a break \N{hot beverage} !Reply *Start* to begin your productivity session"
    def pomodoro(message):
    	client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=message)
    if msg == 'Start':
    	global prodse
    	prodse = msg_received
    	sched = BackgroundScheduler(daemon=True)
    	sched.add_job(pomodoro, 'date', run_date=prod_session, args=[prod_msg])
    	sched.start()
    if msg == 'Done':
    	client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=sched.print_jobs())
    	sched.print_jobs()
    	client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body='Not yet!')
    if msg == 'Focus Left':
    	try:
    		time_left = prodse + datetime.timedelta(minutes=25) - datetime.datetime.now()
    		if time_left.seconds // 60 <= 25:
    			minutes_left = f"You have {time_left.seconds // 60} minutes and {time_left.seconds % 60: 02d} seconds left"
    			client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=minutes_left)
    		else:
    			client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body="Please begin a Productivity session by replying *Start*")
    	except NameError:
    		client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body="Hey wait a minute please while we are processing your request...")

    if msg == "Break":
    	global breakse
    	breakse = msg_received
    	sched = BackgroundScheduler(daemon=True)
    	sched.add_job(pomodoro, 'date', run_date=brek_session, args=[brek_msg])
    	sched.start()
    	sched.get_jobs() 
    if msg == 'Break Left':
    	try:
    		time_left = breakse + datetime.timedelta(minutes=5) - datetime.datetime.now()
    		if time_left.seconds // 60 <= 5:
    			minutes_left = f"You have {time_left.seconds // 60} minutes and {time_left.seconds % 60: 02d} seconds left"
    			client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=minutes_left)
    		else:
    			client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body="Please begin a Break session by replying *Break*")
    	except NameError:
    		client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body="Hey wait a minute please while we are processing your request...")



    
    # Create reply
    if msg == 'Hello':
        resp.message("Hi I am your Pomodoro Bot!\n Reply *Start* to begin your productivity session \N{hourglass}")
        return str(resp)
    
    if msg == 'Menu':
        resp.message("Hi I am your Pomodoro Bot!\n\nReply *Start* to begin your productivity session \N{hourglass}\nReply *Focus Left* to check how many time is left\nReply *Break* to take a break \N{hot beverage}\nReply *Break Left* to check how many time is left")
        return str(resp)
    
    




if __name__ == "__main__":
    app.run(debug=True)
   
