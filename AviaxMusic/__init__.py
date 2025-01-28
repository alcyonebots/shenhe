from ShenheMusic.core.bot import Aviax
from ShenheMusic.core.dir import dirr
from ShenheMusic.core.git import git
from ShenheMusic.core.userbot import Userbot
from ShenheMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
