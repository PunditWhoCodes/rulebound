from fastapi import FastAPI, Response, status
from sqlalchemy import text

from rulebound import __version__
from rulebound.db import get_engine

app = FastAPI(title="Rulebound", version=__version__)


@app.get("/healthz", tags=["ops"])
async def healthz() -> dict[str, str]:
    return {"status": "ok", "version": __version__}


@app.get("/readyz", tags=["ops"])
async def readyz(response: Response) -> dict[str, str]:
    try:
        async with get_engine().connect() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "unavailable", "database": "down"}
    return {"status": "ok", "database": "up"}
