
from loguru import logger
from .encoder._video_encoder import VideoEncoder
from .encoder._image_encoder import ImageEncoder


class OnpremiseEncoder:
    def __init__(
        self,
        redis_data: dict,
    ):
        processor_kwargs = {
            "concurrency": 2,
            "sleep_time": 0.1,
        } 
        if redis_data.get("contentType") == "image":
            logger.debug("image encoder")
            self.encoder = ImageEncoder(
                processor_type="Ray_SleepAndPassProcessor",  # processor_key,
                number_of_processors=4,
                processor_kwargs=processor_kwargs
            )
        else:
            logger.debug("video encoder")
            self.encoder = VideoEncoder(
                processor_type="Ray_SleepAndPassProcessor",  # processor_key,
                number_of_processors=4,
                processor_kwargs=processor_kwargs
            )
        
        logger.debug("encoder init end")
        
    async def run(self, *args, **kwargs) -> bool:
        await self.encoder(*args, **kwargs)
        