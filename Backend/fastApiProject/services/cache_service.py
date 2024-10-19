import aioredis
from ..dbConfig.config import settings


redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)


async def get_cache(key: str):
    return await redis.get(key)


async def set_cache(key: str, value, expire=60):
    await redis.set(key, value, ex=expire)


