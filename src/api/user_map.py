from fastapi.responses import HTMLResponse

from config import app, locations_db
from models import LocationInDb
from services import map_display
import utils


@app.get("/map/{user_id}")
async def get_map_for_user(user_id: int) -> HTMLResponse:
    raw_locs = await utils.db_get_all(locations_db, {"user_id": user_id})
    locs: list[LocationInDb] = utils.convert_dicts_to_type(
        raw_locs, LocationInDb)
    html = map_display.get_map_html(locs)
    return HTMLResponse(content=html)
