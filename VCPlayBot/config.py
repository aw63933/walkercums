import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAq6gYKQ0lneQJqmtYUU4hzN1vqhburrp96X85WVx3KS3iYGnryKfvy09YbzjZZORebEMfDe2_TfjamPxQMCEHwYA2Bs65E_Fbb_X-EFEhr4n5ynLG8O0v6x5EbhBjeiUs9k6HCm1PM4dum5BS_djhfu3xukXxpGpzC2n8FLAZ8IawWmhAaQonWoHlvMLqgWQ5SUBhBEPy_1dpLXduuz7GibOYXO436rQ4DoIxvG5RxlDHTe8H-gGiYs5LdN_Gsh2hgR8OZKkdPYsdlZ8bDb_cKxHDiTC2KCVhFKlegJLtD_Dd-PxKDmXYHn_ZSjiDfq7FtUzFhl3QV30S4_RA1xxEKdzEe4wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1997614166:AAHSbFMLoxyUdzHsnZxlq9eunG7YsKwNKes")
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
