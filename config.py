# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29631986"))
API_HASH = getenv("API_HASH", "1e7dcef8cb0d5358a6fb92d33e3db063")
BOT_TOKEN = getenv("BOT_TOKEN", "8159881433:AAHSLnCGxMgxdwEjqwEoTyMIubCCdNe6IyE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1938805245").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kurd87709:VvKzGj3skdICo7yV@cluster0.hydya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002119482459")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002075605306"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
