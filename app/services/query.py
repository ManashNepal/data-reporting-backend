from fastapi import HTTPException, status
from sqlalchemy import create_engine, text

FORBIDDEN_KEYWORDS = ["insert", "update", "delete", "drop", "alter", "truncate"]

def executor(query : str, params : dict, connection_id : str):
    q_lower = query.lower()

    if not q_lower.strip().startswith("select"):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Only SELECT queries allowed"
        )
    
    if any(word in q_lower for word in FORBIDDEN_KEYWORDS):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Forbidden SQL keywords detected"
        )
    
    engine = create_engine(connection_id) 

    with engine.connect() as conn:
        result = conn.execute(text(query), params)

        rows = result.mappings().all()

    return rows
