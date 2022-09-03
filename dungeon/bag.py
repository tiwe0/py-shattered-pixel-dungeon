from collections import defaultdict
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
    from dungeon.item import Item


class Bag:
    def __init__(self):
        self.items = defaultdict(int)
        self.weight_limit = 50

    def add_item(self, item: 'Item') -> 'bool':
        current_weight = self.weight
        if current_weight + item.weight > self.weight_limit:
            return False
        self.items[item] += 1
        return True

    def drop_item(self, item: 'Item') -> 'bool':
        if item not in self.items or self.items[item] <= 0:
            return False
        self.items[item] -= 1
        if self.items[item] == 0:
            del self.items[item]
        return True

    def iter_item(self) -> 'Iterator[Tuple[Item, int]]':
        for item, number in self.items.items():
            yield item, number

    @property
    def weight(self) -> float:
        total_weight = 0
        for item, number in self.iter_item():
            total_weight += number * item.weight
        return total_weight

