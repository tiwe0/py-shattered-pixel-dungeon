from dungeon.actors.actor import Actor


class Buff:
    def __init__(self, actor: 'Actor'):
        self.actor = actor
        pass

    def act(self, actor: 'Actor'):
        pass


class BuffWithInterval(Buff):
    def __init__(self, actor: 'Actor', interval: int):
        super(BuffWithInterval, self).__init__(actor)
        self.interval = interval
        self._game_turn_clock = 0

    @property
    def clock(self) -> int:
        return self._game_turn_clock

    @clock.setter
    def clock(self, value: int):
        if value >= self.interval:
            self._game_turn_clock = value % self.interval
        else:
            self._game_turn_clock = value

    def act(self, actor: 'Actor'):
        if self.clock == 0:
            self.interval_act(actor)
        else:
            pass
        self.clock += actor.last_spend

    def interval_act(self, actor: 'Actor'):
        pass
