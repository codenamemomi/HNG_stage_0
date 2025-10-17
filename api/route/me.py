from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from api.service.me import get_me_response
from core.settings import settings

router = APIRouter(prefix="", tags=["Profile"])


@router.get("/me", summary="Get profile info with cat fact")
async def get_me():
    response_data = await get_me_response()

    # If Cat Facts API failed and FAIL_ON_CATFACT_ERROR=True
    if response_data.get("status") == "error":
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content=response_data,
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response_data,
    )
