from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC82f4bfbe4ccd026a6251a31b558c7461'
auth_token = '41f8173855a0e2c64250ab5282d6583e'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+917698938566',
                        from_='+14155238886'
                    )

print(call.sid)