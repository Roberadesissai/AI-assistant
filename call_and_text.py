import csv
from twilio.rest import Client
from text_to_speech import TextToSpeech

tts=TextToSpeech()

# Your Twilio account SID and authentication token
account_sid = 'AC10728830974b957e8f23fbae1a262638'
auth_token = '48e58f5c0d8348e8047a6901571c922b'

# Set up the Twilio client
client = Client(account_sid, auth_token)

def send_text_message(tts, message):
    # Look up name in CSV file to get phone number


    # Send the text message
    message = client.messages.create(
        to='3808676081',
        from_='+18775964032',
        body=message
    )

    print("Message sent")

################################################################################################################################################
################################################################################################################################################

def emergency_call():
    """
    Makes a call to 911 using the Twilio API.
    """

    emergency_number = "3808676081"

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=emergency_number,
        from_='+18775964032',
        url="http://demo.twilio.com/docs/voice.xml"
    )

    print(f"Dialing {emergency_number}...")

    # If the call was successfully initiated, return the call SID
    return call.sid

emergency_call()





    