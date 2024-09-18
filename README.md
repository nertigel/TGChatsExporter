# TGChatsExporter for Telegram
This is a telegram user-bot based off the [Pyrogram](https://github.com/pyrogram/pyrogram) library in Python3. 

# How it works

The user-bot will iterate through all dialogs/chats that could be found and saves chats that are private. Great in-case your user has been deleted and you would like to contact your previuos private chats.

# Installation

You can run this bot on your own, install the required lib by running this command: 

```bash
pip install pyrogram
```

# Configuration

In the `main.py` file you will find `api_id` and `api_hash` variables at lines `10-11`, get your [API credentials from Telegram's official website](https://my.telegram.org/auth).

Now you can simply run the bot by running `main.py`
