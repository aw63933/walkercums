import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAf2Ytkwtotz7h2Pvfr5ZbtJn93FU44pDOiBe0PTofq2ZzG94bOpemi12FCuAXggSBUdY6JsCwdDhSgQlP8PR2lHw1pdLrhh07WfvbZlb2katQqlCrDtUR8obKRIQMBakjdY5GAUHpdlQiH3E_E_bWzaHuCFjjduZn9_ETT8u3246WQPrN_zoo1NJi5ggJ2ozmiU-ycM8Yz2hSK9zUbh-J9-oiSXUrlkDVTVk9Ac43YzFo9MlN-GzwWyZAVwvSoeiDXEyl_vvdh3HF9J5oOGV8l6wW1ed79ubsAcQb78VgwzCJuVwe-N9e6qJL2z0I6nol3PG1oxawtWg4JskceAygTdzEe4wA")
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
