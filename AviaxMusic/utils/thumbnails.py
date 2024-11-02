import os

async def gen_thumb(videoid: str):
    try:
        # Specify the path to your custom image
        custom_image_path = "AviaXMusic/assets/shenhe.png"
        
        # Ensure the image file exists
        if not os.path.isfile(custom_image_path):
            raise FileNotFoundError(f"Custom image not found at {custom_image_path}")

        # Return the path to your custom image
        return custom_image_path

    except Exception as e:
        logging.error(f"Error fetching custom thumbnail for video {videoid}: {e}")
        return None
