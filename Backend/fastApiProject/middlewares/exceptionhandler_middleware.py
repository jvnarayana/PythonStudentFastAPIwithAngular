from fastapi import Request, HTTPException
import logging

logger = logging.getLogger(__name__)


async def exception_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except HTTPException as exc:
        logger.error(f"HTTPException: {exc.detail}")
        raise
    except Exception as exc:
        logger.error(f"Exception: {exc}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
