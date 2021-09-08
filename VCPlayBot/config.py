import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBODEgynNYjivyDhKz5ekwjaDd9OMEuc4xnT-UYZHVCOcbHTP66KPbwQyNKSIKtMN7VW71Joj4eeEXvSh1UU4TDj_T8pvMG4V2sUQuWcd9T6kXJpDxG8am3G0XZGuQtdP9B36XLLuTb7r8Pz1C2gjAvqNPnIgMEgNz1J4yYp2CBTeVEqAN8MoDi0KsVmSnf8TlH-rJMCidjCcWCjieLSvbZM1o08QfxxqKboo93tjuecaH-D08QAzaq2sFt0bqTZ-LBDHnm7iLGEPTkzi5_32NvxNYtmQ1L_32pepL4ho55bXwK2kuGHNLHMqQla49f4lYHEuFH7_V0kl_BjuA4zOnwdzEe4wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1997614166:AAH4DQux1RwRZBs9mLrVlxK-_ayTlFGLtdA")
BOT_NAME = getenv("BOT_NAME", "The VC Music Player")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kernel4vince")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/967cad983cc374a730908.png")
admins = {}
API_ID = int(getenv("API_ID", 7342182))
API_HASH = getenv("API_HASH", "a80ca7acb06d0cb64a967ba33ef1e536")
BOT_USERNAME = getenv("BOT_USERNAME", "thewalkermusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "thewalkermusic")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kernel4vincechat")
PROJECT_NAME = getenv("PROJECT_NAME", "thewalkermusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/aw63933")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "JPAJID-ITLULC-BFRVKB-ANKJDS-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001183867251")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1362497646 1999707875").split()))
