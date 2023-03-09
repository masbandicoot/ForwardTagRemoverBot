# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
# Copyright (C) 2023 by Abdul Razaq <https://github.com/Artis7eeR>
# ForwardTagRemoverBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ForwardTagRemoverBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    SOURCE = "https://www.youtube.com/channel/UCPVeBAZTd3D44kX8e8mXTFg"
    START_TEXT = """
Hi [{}](tg://user?id={}) 
I am Masbandicoot Bot Assistant :)."""
    HELP_TEXT = "I only forward Masbandicoot Testimoni"
