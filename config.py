import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", 29013102))
API_HASH = os.environ.get("API_HASH", '6525d7b0bbda6e9369db2ee3c7cf7e09')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '5947068251:AAG3jPQFy7wdkh0vJa_7EkUX-FwKIaK_hjs')
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
OWNER_ID = int(os.environ.get("OWNER_ID", "5232827456"))
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Shortener")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://shortingly:154gS9u6XUWAjjp8@cluster0.l7rss4b.mongodb.net/?retryWrites=true&w=majority")
# Optionnal variables
BROADCAST_AS_COPY = is_enabled((os.environ.get('BROADCAST_AS_COPY', "False")), False)
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
BIN_CHANNEL = os.environ.get("BIN_CHANNEL", -1001879609154)
#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
BASE_SITE = "shortingly.in"

if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
