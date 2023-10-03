import random
from typing import Any

import folium

from models import LocationInDb
from config import app


COLORS = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
          'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
          'darkpurple', 'pink', 'lightblue', 'lightgreen']


def create_map(locations: list[LocationInDb]) -> folium.Map:
    if locations:
        loc = locations[0]
        m = folium.Map(
            zoom_start=8,
            location=[loc.latitude, loc.longitude],
            # tiles="http://127.0.0.1:8000/static/map.json",
            # attr='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            max_zoom=24,
        )
    else:
        m = folium.Map(
            max_zoom=24,
        )
    for loc in locations:
        folium.Marker(
            location=[loc.latitude, loc.longitude],
            tooltip=loc.name,
            popup=loc.name,
            icon=folium.Icon(
                icon="globe",
                color=random.choice(COLORS)),
        ).add_to(m)

    return m


def get_map_html(locations: list[LocationInDb]) -> str:
    m = create_map(locations)
    html: str = m.get_root().render()
    return html


def get_map_bytes(locations: list[LocationInDb]) -> bytes:
    html: str = get_map_html(locations)
    html_bytes = html.encode("utf-8")
    return html_bytes
