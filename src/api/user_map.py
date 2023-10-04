from fastapi.responses import HTMLResponse
from fastapi import Request, Response
from bson import ObjectId

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
            "map_style": MAPBOX_STYLE,
            "icons": [item.dict() for item in utils.get_all_icons()],
            "default_icon": "marker.svg"
        })


@app.get("/default/map/{user_id}")
async def get_default_for_user(user_id: int) -> HTMLResponse:
    raw_locs = await utils.db_get_all(locations_db, {"user_id": user_id})
    locs = utils.convert_dicts_to_type(raw_locs, LocationInDb)
    html = map_display.get_map_html(locs)
    return HTMLResponse(content=html)


@app.delete("/location/{loc_id}")
async def delete_location(
    loc_id: str,
) -> Response:
    res = await locations_db.delete_one({"_id": ObjectId(loc_id)})
    if res.deleted_count:
        return Response(status_code=200)
    return Response(status_code=400)
