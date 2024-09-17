import logging
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType
from pyrogram.types import User

logging.basicConfig(level=logging.INFO)

# Add your API ID, API Hash, and Session Name
api_id="api_id"
api_hash="api_hash"
session_name = 'session'

app = Client(session_name, api_id, api_hash)

def get_user_details(user: User):
    details = {
        'chat_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': getattr(user, 'last_name', ''),
        'phone_number': getattr(user, 'phone_number', 'None'),
        'is_contact': getattr(user, 'is_contact', False),
        'status': getattr(user, 'status', 'None'),
    }
    return details

def write_details_to_file(details_list):
    with open("chats_details.txt", "w", encoding="utf-8") as file:
        for details in details_list:
            file.write(f"Chat ID: {details['chat_id']}\n")
            file.write(f"Username: {details['username']}\n")
            file.write(f"First Name: {details['first_name']}\n")
            file.write(f"Last Name: {details['last_name']}\n")
            file.write(f"Phone Number: {details['phone_number']}\n")
            file.write(f"Is Contact: {details['is_contact']}\n")
            file.write(f"Status: {details['status']}\n")
            file.write("="*30 + "\n")

@app.on_message()
def main(client, message):
    chat_details_list = []

    try:
        for dialog in app.get_dialogs():
            print(dialog.chat.type)
            if dialog.chat.type == ChatType.PRIVATE:
                user_details = get_user_details(dialog.chat)
                chat_details_list.append(user_details)
    except FloodWait as e:
        logging.warning(f"FloodWait: Waiting for {e.value} seconds before continuing.")
        app.idle(sleep=e.value)
    
    write_details_to_file(chat_details_list)
    logging.info("Details written to chats_details.txt")

if __name__ == "__main__":
    app.start()
    main(app, None)
    app.stop()