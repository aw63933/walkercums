import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBlquC4seP6H6TxHo0Ug4VaE-ReFaNRn65RvJN2GbOIb1BH9dv8FzBNt1mFmeayFb00e1uqnaZ3vCgoVjItiSek7u8tWV0sLBG02My7TIo-MJwAsYDmtIWyxOP8VYDWmZgPlIDcPvAucwDaipvc0ywcr6USr6jhr9sJZ0A4uJJiXBTXfLRb_lM0FhPUmwbTbsaEEgzy1Qw0M7_21qtuwGyg50o6OYQvtn8eNUhQheXz-KVzrn1omSCdCdJIr4N30fyuK3QJ6rKCcFpJ3u9yQtssUUVfYY6--eiPH3WLUcYZd8OnNfzXEjSZJhy03Ar8Adr3xab8F9SAVfjsLpbuNxOFdzEe4wA")
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
