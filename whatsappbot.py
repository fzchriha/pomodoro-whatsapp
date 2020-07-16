from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import schedule
import time
import emoji 
app = Flask(__name__)


account = "AC9eab8284718f0d0e57962dd4ec243fc0"
token = "86a41ef3e3aad5e3f8d61cf104d40309"
client = Client(account, token)

# message = client.messages.create(to=user_number(), from_="whatsapp:+14155238886",
#                                  body="Hello there!")
def print_hi():
    print("Hello")
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

                            
    # Fetch the message
    msg = request.form.get('Body')
    phone_number = request.form.get('From')

    # Reply after session
    prod_session = 60 * 25
    brek_session = 60 * 5
    prod_msg = "You did a great job! Reply *Break* to take a break"
    brek_msg = "Hmm feels good to have a break \N{hot beverage} !Reply *Start* to begin your productivity session"
    if msg == 'Start':
        time.sleep(prod_session)
        client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=prod_msg)
    elif msg == "Break":
        time.sleep(brek_session)
        client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=brek_msg)

    resp = MessagingResponse()
    # Create reply
    if msg == 'Hello':
        resp.message("Hi I am your Pomodoro Bot!\n Reply *Start* to begin your productivity session \N{hourglass}")
        return str(resp)
    

    elif msg == 'Test':
        resp.message("This is a test")
        for i in range(10):
            print(i)
            time.sleep(6)     
        return str(resp)
    resp.message("Hello, I am your Pomodoro Bot \N{tomato}")




if __name__ == "__main__":
    app.run(debug=True)
    
# def job_that_executes_once():
#     # Do some work ...
#     return schedule.CancelJob

# schedule.every().day.at('22:30').do(job_that_executes_once)

# Threads Flas