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
from models import LocationInDb
from services import map_display


@app.get("/map/{user_id}")
async def get_default_for_user(user_id: int, request: Request) -> HTMLResponse:
    raw_locs = await utils.db_get_all(locations_db, {"user_id": user_id})
    return templates.TemplateResponse(
        "map.html",
        {
            "request": request,
            "locations": raw_locs,
            "access_token": MAPBOX_TOKEN,
            "map_style": MAPBOX_STYLE
        })


@app.get("/default/map/{user_id}")
async def get_default_for_user(user_id: int) -> HTMLResponse:
    raw_locs = await utils.db_get_all(locations_db, {"user_id": user_id})
    locs = utils.convert_dicts_to_type(raw_locs, LocationInDb)
    html = map_display.get_map_html(locs)
    return HTMLResponse(content=html)
