import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBvK4CMzVcwnpAZsY7mvSPRkerXrx5iK9r4UixH0u7pXldBhRHXofXR3Qyz8XdBV-X5vuKTEekTPk0dGyAyTCxrCDvvsBKrvZ8w3yRP-b9AxixGOuBXe6XoOy73CqAwPukAYmx38uXWmZ09Ju1Y53g0U8i7yaVuteb5SY508gcHM4qk3PoOcAQlwRmP2LoNZDNk6tfPaL6ZayrlQ937t_QSrff020Se1MNJfa-lXmvxjXlRECSCd1RqR_wSh0XoK3nqt7y8hXJiq253KnGyAZLOT_tzcGhQ4kTE89rN9xSkWgm2VXj-ECbQ7ikdQR4E1tL5o7IDi4z6LK2ijOqdIsgedzEe4wA")
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
