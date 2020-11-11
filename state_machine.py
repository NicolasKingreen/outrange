import random
from math import sqrt

class StateMachine():

    def __init__(self):

        self.states = {}
        self.active_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return

        self.active_state.do_actions()

        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()

        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()
        self.active_state.npc.prep_state_label()


class State:

    def __init__(self, name):
        self.name = name

    def do_actions(self):
        pass

    def check_conditions(self):
        pass

    def entry_actions(self):
        pass

    def exit_actions(self):
        pass

    def __repr__(self):
        return self.name


class NPCStateExploring(State):

    def __init__(self, npc):
        super().__init__("exploring")
        self.npc = npc

    def do_actions(self):
        if random.randint(1, 300) == 1:
            self._set_npc_random_destination()

    def _set_npc_random_destination(self):
        dx = random.uniform(-150, 150)
        dy = random.uniform(-150, 150)
        self.npc.destination = (self.npc.x + dx, self.npc.y + dy)
        # print(f"{self.npc.destination}")

    def check_conditions(self):
        player = self.npc.world.player
        distance_to_player = sqrt((self.npc.x - player.x) ** 2 + (self.npc.y - player.y) ** 2)
        if distance_to_player < self.npc.detection_range:
            return "seeking"

    def entry_actions(self):
        self.npc.speed = 0.1 + random.uniform(0, 0.05)
        # self._set_npc_random_destination()


class NPCStateSeeking(State):

    def __init__(self, npc):
        super().__init__("seeking")
        self.npc = npc

    def do_actions(self):
        self.npc.destination = (self.npc.world.player.x, self.npc.world.player.y)

    def check_conditions(self):
        player = self.npc.world.player
        distance_to_player = sqrt((self.npc.x - player.x) ** 2 + (self.npc.y - player.y) ** 2)
        if distance_to_player > self.npc.detection_range:
            return "exploring"

    def entry_actions(self):
        self.npc.speed = 0.2

    def exit_actions(self):
        self.npc.destination = self.npc.x, self.npc.y
