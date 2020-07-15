from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import schedule
import time
import emoji 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi I am your Pomodoro Bot! Reply 'start' to begin your productivity session"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Fetch the message
    msg = request.form.get('Body')
    resp = MessagingResponse()
    # # Create reply
    
    if msg == 'Hello':
        resp.message("Hi I am your Pomodoro Bot!\n Reply *Start* to begin your productivity session \N{hourglass}")
        return str(resp)
    elif msg == 'Start':
        print("hey")
        resp.message("You did a great job! Reply *Break* to take a break")
        time.sleep(6)
        return str(resp)
    elif msg == "Break":
        print("hey")
        resp.message("Hmm feels good to have a break \N{hot beverage} !Reply *Start* to begin your productivity session")
        time.sleep(6)
        return str(resp)

    resp.message("Hello, I am your Pomodoro Bot \N{tomato}")
    print(emoji.demojize('⌛️'))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)