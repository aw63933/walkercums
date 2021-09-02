import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQDDf1j6quqjgKzMfREJ7I8XRIaMVkpFE6zAkQdyselCDlOPLsFkOXCbadwvuiWw8vAEZBfeA_zBQ3aQxRdisQ4gcsCn895S1K47re1di60OuUNIHKeQTz1ex8FowrJ2EHeJJuWQXHr_w6DS3S02TZ8xpUKvgKlJ-giwfUBf32lH-EzqM-r8COjoqbC51rclpJ7SUFYrzry0ITRyjrIXxjw-dapjTtQ8-wtqonkyjd9j7CIJe4am7AAjr1GbfHj9KxleFA0HLzaAAZJannQN6TrHu1BUnqd8-8t4jqH7wANqYa_D3fpVccGycr9q3AwdNja_11UgPyFWc-TWfGwWObMcZ1WA6wA")
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
