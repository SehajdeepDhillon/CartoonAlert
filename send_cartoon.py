from config import client, r

def send_message(cartoon_url):
    phone_numbers = r.smembers('phone_numbers')
    if not phone_numbers:
        print("No phone numbers found in Redis")
        return
    
    for phone_number in phone_numbers:
        phone_number = phone_number.decode('utf-8')
        try:
            message = client.messages.create(
                to=phone_number,
                from_='+12097200651',
                body=f'New cartoon available! {cartoon_url}'
            )
        except Exception as e:
            print(f"Failed to send message to {phone_number}: {e}")