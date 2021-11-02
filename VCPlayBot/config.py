import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA1IoszdqWio2HPyoIkVJhQCXym9e-P8NyaVCFibeWEIcyydpZ8RIw6mhqcr898lHPqcvnI_ROZktCBUwtvcO5N37D3Y8M_7IOE4nDx9pHJO70T27v4JoXGNX6mSEGcuqR4Rnz00NPx2zCV5MD5UucnOfDStV5W5yhsVgA4t5nwVR2UbRSBMo75liQzJJ2HRZuPYq-fgX6X8gOzNCNh5zvdmeFiEIxDCWH0IAtjUEV0blNxxQ_g6hw4Mbnrln05N8w_Tw95aAF6fK_tEd7L9pCiMdS6HEazut8e1u-CBRTWUXtOZjUhoBvHMzLRbnOXVi5AMYpt2ZvW6qs4H6xlBm1TdzEe4wA")
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
