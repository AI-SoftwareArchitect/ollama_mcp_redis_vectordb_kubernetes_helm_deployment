import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def get_context_from_redis(key: str) -> str:
    return r.get(key)

def set_data_in_redis(key: str, value: str):
    r.set(key, value)
