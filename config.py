import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29872536"))
API_HASH = getenv("API_HASH", "65e1f714a47c0879734553dc460e98d6")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7939429941:AAEmgu-4hyjMOYKqMtVsVOuS5cdLXvM7iYI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://shenhe:shenhe@telegram.ysvwj.mongodb.net/")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002183841044"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6698364560"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nxivm-bots/shenhe.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AlcyoneBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alcyone_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "fcc60046623448ac8aec5ec95c4d2578")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "ddbb914ec49c48b88375f690cf40157c")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BQF_85kAa7RtgvpH7ZL4ZmJiC8COn1o_zK1BBL52NMrrbj2EGRbyyw2yT1A3pYjNrySnf8gp60HtHWqKlzR8nMRuvaCXIF99CcPpWDne6C5Vj6iYKIUvKzUt7-bSTV1BrcftuUzWX9Eg1mA9xciNlcXXSmhJXrvFhOMMfhY5bGRlG7QHcuwlhfMFJbqgXstSF2zZDbLRrvUnZgEUg5JkzoTxMkRUwdY_rDlYmbBxFHIpuVWQRgtduzfgflgA9aN2kgJpOyW5NwzE3qb1SA68Nv5ShTrKOM6hYuOuH2Aabxo8MYXBQ-g2x8OSiOSkjDlWpFb404fsz1hEd_-dZBZGnqjwl99nRAAAAAGRn950AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/T4P3TGM/file-1060.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/T4P3TGM/file-1060.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
STATS_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
STREAM_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/T4P3TGM/file-1060.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
