import random
from typing import Tuple, Union, Iterable, List, Optional
from copy import deepcopy
import re


class Dice:
    def __init__(self, desc: 'str' = '0d0+0'):
        self.desc = desc
        self.dice_num, self.dice_side, self.dice_fix = self.parse_desc(desc)

    def __repr__(self):
        return f"\ndice_num    : {self.dice_num}\ndice_side   : {self.dice_side}\ndice_fix    : {self.dice_fix}\ndice_expect: {self.expect}"

    def __add__(self, other: 'Dice'):
        return MultipleDice([self, other])

    @property
    def expect(self):
        return (float(1+self.dice_side)/2) * self.dice_num + self.dice_fix

    def roll(self, times: 'int' = 1) -> 'Union[int, List[int]]':
        if times == 1:
            return self.roll_once()
        else:
            return [self.roll_once() for _ in range(times)]

    def roll_once(self) -> 'int':
        result = self.dice_fix
        for _ in range(self.dice_num):
            result += random.randint(1, self.dice_side)
        return result

    @classmethod
    def parse_desc(cls, desc: 'str') -> Tuple[int, int, int]:
        if '+' not in desc:
            desc += '+0'
        desc_num, desc_side, desc_fix = [int(s.strip()) for s in re.split(r'd|\+', desc)]
        return desc_num, desc_side, desc_fix


class MultipleDice:
    def __init__(self, dices: 'List[Dice]' = []):
        self.dices: 'List[Dice]' = dices

    def __add__(self, other: 'Union[Dice, MultipleDice]'):
        if isinstance(other, Dice):
            dices = deepcopy(self.dices)
            dices.append(other)
            return MultipleDice(dices)
        if isinstance(other, MultipleDice):
            this_dices, other_dices = deepcopy(self.dices), deepcopy(other.dices)
            result_dices = this_dices + other_dices
            return MultipleDice(result_dices)

    def __len__(self):
        return len(self.dices)

    def __repr__(self):
        return '\n'.join([repr(d) for d in self.dices])

    def roll_once(self):
        return sum([dice.roll_once() for dice in self.dices])

    def roll(self, times: 'int' = 1) -> 'Union[int, List[int]]':
        rolls = [self.roll_once() for _ in range(times)]
        if times == 1:
            return rolls[0]
        else:
            return rolls
