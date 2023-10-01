from pathlib import Path
import folium

from models import LocationInDb


def create_map(locations: list[LocationInDb]) -> folium.Map:
    m = folium.Map()
    for loc in locations:
        folium.Marker(
            location=[loc.latitude, loc.longitude],
            tooltip=loc.name,
            popup=loc.name,
            icon=folium.Icon(icon="globe"),
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
