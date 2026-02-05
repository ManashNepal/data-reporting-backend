import hashlib 
import json 
import time 

_CACHE = {}

def make_cache_key(query:str, params:dict, connection_id:str):
    raw = f"{connection_id}:{query}:{json.dumps(params, sort_keys=True)}"
    return hashlib.sha256(raw.encode()).hexdigest()

def get_cache(key:str):
    entry = _CACHE.get(key)

    if not entry:
        return None 
    
    value, expires_at = entry 
    if time.time() > expires_at:
        del _CACHE[key]
        return None

    return value 

def set_cache(key:str, value, ttl : int = 300):
    _CACHE[key] = (value, time.time() + ttl)