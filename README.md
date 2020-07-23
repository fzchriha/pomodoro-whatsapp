# Pomodoro in WhatsApp

A pomodoro bot for whatsappp

#Technologies used:

*Twilio API (Beta)
*Flask

# Usage:

On WhatsApp text **join should-smooth** to **+1 (415) 523-8886**

# Contribute to this project:

* Fork this github repository
* Clone this github repository

```pip install -r requirements.txt```

```python whatsappbot.py```

# Problems faced while building this project:

** Problem 1 **
* Description : Scheduling the bot reply after 25min or 5min

* Reason: Twilio needs to return an http response to /sms within 8 seconds, thus performing ```time.sleep(8)``` or using schedule doesn't work

* Solution: Instead of returning a response, the code sends a one way client message, which is tied to the users message

 i.e: If the user sends **Start** the program sends a one way client message which will be scheduled to run after 25min ( See lines [ 39 - 46 ] in whatsappbot.py ) 
 
** Problem 2 **
