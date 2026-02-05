from fastapi import APIRouter 

from app.schemas.query import QueryRequest
from config.cache import make_cache_key, get_cache, set_cache
from app.services.query import executor

router = APIRouter(prefix = "/query", tags = ["Query"])

@router.post("/")
def run_query(req : QueryRequest):
    cache_key = make_cache_key(
        req.query, req.params, req.connection_id
    )

    cached = get_cache(cache_key)

    if cached:
        return {
            "source" : "cache",
            "data" : cached
        }
    
    result = executor(req.query, req.params, req.connection_id)

    set_cache(cache_key, result, 300)

    return {
        "source" : "database",
        "data" : result
    }

