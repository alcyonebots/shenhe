import os
import logging
import random
from PIL import Image

thumbnail_paths = [
    "ShenheMusic/assets/shenhe.png", 
    "ShenheMusic/assets/shenhe1.png" 
]

async def gen_thumb(videoid: str):
    try:
        if os.path.isfile(f"cache/{videoid}_v4.png"):
            return f"cache/{videoid}_v4.png"
        
        selected_thumbnail_path = random.choice(thumbnail_paths)
        
        youtube = Image.open(selected_thumbnail_path)
        
        background_path = f"cache/{videoid}_v4.png"
        youtube.save(background_path)
        return background_path
    except Exception as e:
        logging.exception(f"Error generating thumbnail for video {videoid}: {e}")
        return None
