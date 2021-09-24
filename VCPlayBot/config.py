import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC4vJLE5x5lqvWX7IfGBJCOGFhMP61QcP7RBteAYgiTBg537C43UuFko3C9ZLwsXlrq3Cqt6AtLiTOT45pb4a5N_AFVIYmKrp88b-ycEIgsWYVZa3v9Xjywt-wD1cPL_ClaUuu8dBo4ZGfP8qzPDN3V6a08DDFNKbL4o_uEEt3DXrucxFedfUcAEKK_byrh6Ll7JMLWUUxfN3t9aW08g3E5Zt6GpNDV8jcnbwYYT_i8DjK6x186npZqceHQUNGWZ-PyY9i_uH9l-GrLIV88E794BMxZ0vtvdgAuNJTWavskqfYYxyv-wXeMGrhgc0qMcLz0hggv9M8cXp64Zgr25jz6dzEe4wA")
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
