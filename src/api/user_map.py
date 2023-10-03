from fastapi.responses import HTMLResponse
from fastapi import Request

from config import (
    app,
    locations_db,
    templates,
    MAPBOX_TOKEN,
    MAPBOX_STYLE,
)
import utils


@app.get("/data/{user_id}")
@app.get("/map/{user_id}")
async def get_map_for_user(user_id: int, request: Request) -> HTMLResponse:
    raw_locs = await utils.db_get_all(locations_db, {"user_id": user_id})
    return templates.TemplateResponse(
        "map.html",
        {
            "request": request,
            "locations": raw_locs,
            "access_token": MAPBOX_TOKEN,
            "map_style": MAPBOX_STYLE
        })
