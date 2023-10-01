import random

import folium

from models import LocationInDb


COLORS = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
          'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
          'darkpurple', 'pink', 'lightblue', 'lightgreen']


def create_map(locations: list[LocationInDb]) -> folium.Map:
    m = folium.Map()
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
