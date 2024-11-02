import os
import logging
from PIL import Image

async def gen_thumb(videoid: str):
    try:
        if os.path.isfile(f"cache/{videoid}_v4.png"):
            return f"cache/{videoid}_v4.png"

        default_thumbnail_path = "AviaxMusic/assets/shenhe.png"
        
        youtube = Image.open(default_thumbnail_path)

        background_path = f"cache/{videoid}_v4.png"
        youtube.save(background_path)
        
        return background_path

    except Exception as e:
        logging.exception(f"Error generating thumbnail for video {videoid}: {e}")
        return None
