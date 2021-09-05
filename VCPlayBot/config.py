import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAUpLAomJjgVfBDOQ2CvijT9TMEORCKFEOwEJCe4Y9Jn_0MFZ_MGUceS1NooDcsV7l6xu3qCUV8xTMzesZjKPJ5ZxbbmFLMQDVKYkqIq200mcRvyWE0bMQliS8ajo5rVq3yIqrsu3eP-wERC_m3l1kAuHOp3UoTo01-h299tcz4DazNWKh9gGXKN1ieMOKh8tKhYAPhU3i16zWk3PZ2ChDtbfgTM2u-4gvkJYh0z3gH5urwrZPQkcYTNEMt-T8CaA13iSk8VwQ6trd6WVcd3QqFbh-c0ije9KPnbDF1aRSsYeSRzGs2xT2xIQ3RHY_y6VLDW8tmKcrT9N9J23Nes1S5Z1WA6wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1653789420:AAGjLfTKP-7ZeYjO26VTt5HaDNGDthUVjJY")
BOT_NAME = getenv("BOT_NAME", "The VC Music Player")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kernel4vince")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/967cad983cc374a730908.png")
admins = {}
API_ID = int(getenv("API_ID", 5067596))
API_HASH = getenv("API_HASH", "0c1c4340f006ea05763e3fe42da32b4f")
BOT_USERNAME = getenv("BOT_USERNAME", "thevcmusicplayerbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "thevcmusicplayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kernel4vincechat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/aw63933")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "CLDRFM-ZUWOQR-CKDGPB-QTRXGH-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001183867251")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1362497646 1733656811").split()))
