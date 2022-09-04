from typing import Optional, TYPE_CHECKING
from dungeon.components import TileComponent
from dungeon.components.HUD import StatusPanel, HealthBar, BagButton, WaitButton, SearchButton

from dungeon.input_handler import MainEventHandler, InventoryEventHandler

if TYPE_CHECKING:
    from dungeon.engine import Engine


class UI(TileComponent):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.engine: 'Optional[Engine]' = None
        self.inventory_panel: 'Optional[TileComponent]' = None

    def add_inventory_panel(self, component: 'TileComponent'):
        self.inventory_panel = component
        self.add_child(component)

    def toggle_inventory(self):
        if self.inventory_panel:
            self.inventory_panel.activate = not self.inventory_panel.activate
        # TODO 下面的代码不应该出现在这里
        if self.inventory_panel.activate:
            self.engine.input_handler = InventoryEventHandler.instance
        else:
            self.engine.input_handler = MainEventHandler.instance
