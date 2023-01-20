#!/usr/bin/env python3
import copy

import tcod

from engine import Engine
from entity import Entity
import entity_factories
from procgen import generate_dungeon, generate_streets
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    street_max_size = 10
    street_min_size = 6
    max_rooms = 30

    max_side_streets = 4
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)

    game_map = generate_streets(
         max_rooms=max_rooms,
         street_min_size=street_min_size,
         street_max_size=street_max_size,
         map_width=map_width,
         map_height=map_height,
 	       max_side_streets=max_side_streets,
         player=player
    )
    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)

if __name__ == "__main__":
    main()
