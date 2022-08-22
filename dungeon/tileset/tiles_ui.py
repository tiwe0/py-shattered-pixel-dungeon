from utils.tile_load import load_tile


class Tiles:

    class UI:
        pass

    class Interface:
        interfaces_path = "assets/interfaces/"
        status_panel = load_tile(interfaces_path+"status_pane.png", (0, 0), (128, 34))
        health_bar = load_tile(interfaces_path+"status_pane.png", (0, 36), (50, 4))
        shield_bar = load_tile(interfaces_path+"status_pane.png", (0, 40), (50, 4))
        experience_bar = load_tile(interfaces_path+"status_pane.png", (0, 44), (16, 1))

        bag_button = load_tile(interfaces_path+"toolbar.png", (0, 0), (24, 26))
        wait_button = load_tile(interfaces_path+"toolbar.png", (24, 0), (20, 26))
        search_button = load_tile(interfaces_path+"toolbar.png", (44, 0), (20, 26))
        single_slot = load_tile(interfaces_path+"toolbar.png", (64, 0), (22, 24))
        double_slot = load_tile(interfaces_path+"toolbar.png", (86, 0), (39, 24))
        four_slot = load_tile(interfaces_path+"toolbar.png", (128, 0), (21, 23))


