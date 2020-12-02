# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC82f4bfbe4ccd026a6251a31b558c7461'
auth_token = '41f8173855a0e2c64250ab5282d6583e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Employee has been registered successfully with treebo hotels",
                     from_='+447403941368',
                     to='+917698938566'
                 )

print(message.sid)
