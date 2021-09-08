import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCsLnFE-qWN-k7uRQ5oNTW0XFpFO5LpwLN-hmemmqegezM7OPr1Jbdu7Xm7Sl69LoVfs9U_RHTAm1yvU6tLwvktxHx4Blq-IwafjzLiAp3PgkDgFoIEUXa0goq7RXyA1CuBtn7t20VgkfFDi1KNPqZ9BDV2-wi3Pe4bgCX5K_ZiF_8ZgaNDVCjJqB4mNtcJwy3JfIOg-9jHn-A8_yKO45bFsYR6_Rmy8u22dwyTAcTYj9EfEVQofOHaneKyVCnwF37Qp2Dzb1TOuhtz0cCAXP5Xx5ig1gpUzn_q2fai3flwYGtDspCfLR01Udt48ZBkhbKs1OXC6KC5vLV2weSwmdyrZ1WA6wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1997614166:AAH4DQux1RwRZBs9mLrVlxK-_ayTlFGLtdA")
BOT_NAME = getenv("BOT_NAME", "The VC Music Player")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kernel4vince")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/967cad983cc374a730908.png")
admins = {}
API_ID = int(getenv("API_ID", 5067596))
API_HASH = getenv("API_HASH", "0c1c4340f006ea05763e3fe42da32b4f")
BOT_USERNAME = getenv("BOT_USERNAME", "thewalkermusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "thewalkermusic")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kernel4vincechat")
PROJECT_NAME = getenv("PROJECT_NAME", "thewalkermusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/aw63933")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "CLDRFM-ZUWOQR-CKDGPB-QTRXGH-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001183867251")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1362497646 1733656811").split()))
