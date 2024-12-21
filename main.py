# install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# twilio credentials
account_sid='your-account-sid'
auth_token='your-auth-token'

client = Client(account_sid, auth_token)

# define send message func
def send_whatsapp_message(receipent_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{receipent_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured.')

#user-input
name = input('Enter the receipent name: ')
receipent_number = input('Enter the receipent number with country code: ')
message_body = input('Enter the message you want to send to {name}: ')

#parse date, time and calculate delay
date_str = input('Enter the date tomsend the message (YYYY: MM: DD): ')
time_str = input('Enter the time to send the message (HH: MM in 24 hours format): ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

#wait until the scheduled time
time.sleep(delay_seconds)

#send the message
send_whatsapp_message(receipent_number, message_body)
