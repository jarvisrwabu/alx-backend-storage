import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        """Initialize redis client and flush db."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return a string from data argument."""
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis with the key
        return key
