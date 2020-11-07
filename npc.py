import math
import pygame as pg

from animator import Animator
from entity import Entity
from state_machine import StateMachine, NPCStateExploring, NPCStateSeeking

class NPC(Entity):

    def __init__(self, game_instance, name):

        super().__init__(game_instance, name)

        self.brain = StateMachine()

        self.detection_range = 300

        self.destination = (0, 0)
        self.movement_direction = (0, 0)
        self.speed = 0.
        self.hp = 12

    def prep_state_label(self):
        self.state_surface = self.game_instance.settings.font.render(f"{self.brain.active_state}", True, (255, 255, 255))
        self.state_rect = self.state_surface.get_rect()
        self.state_rect.center = self.rect.centerx, self.rect.y - 16

    def update(self, dt):
        super().update()
        self.state_rect.center = self.rect.centerx, self.rect.y - 16
        self.animator.update(dt)
        self.brain.think()

        distance = math.sqrt((self.destination[0] - self.rect.x) ** 2 + (self.destination[1] - self.rect.y) ** 2)
        if distance > 5:
            v_length = math.sqrt((self.destination[0] - self.rect.x) ** 2 + (self.destination[1] - self.rect.y) ** 2)
            if v_length != 0:
                self.movement_direction = ((self.destination[0] - self.rect.x) / v_length, (self.destination[1] - self.rect.y) / v_length)

            if self.movement_direction[0] or self.movement_direction[1]:
                vector_size = math.sqrt(self.movement_direction[0] ** 2 + self.movement_direction[1] ** 2)
                normalized_movement_direction = list(self.movement_direction)
                normalized_movement_direction[0] /= vector_size
                normalized_movement_direction[1] /= vector_size
                self.x += normalized_movement_direction[0] * self.speed * dt / 1
                self.y += normalized_movement_direction[1] * self.speed * dt / 1
                self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        super().draw(surface)
        if self.game_instance.settings.draw_debug:
            surface.blit(self.state_surface, self.state_rect)
            pg.draw.circle(surface, (255, 100, 100), self.rect.center, self.detection_range, 1)


class RangerNPC(NPC):

    def __init__(self, game_instance, spawn_location):
        super().__init__(game_instance, "ranger_npc")
        self.rect = pg.Rect(spawn_location, (64, 104))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self._load_images_from_sprite_sheet("data/images/ranger.png")
        self.animator = Animator(self, self.images)

        exploring_state = NPCStateExploring(self)
        seekings_state = NPCStateSeeking(self)

        self.brain.add_state(exploring_state)
        self.brain.add_state(seekings_state)

        self.brain.set_state("exploring")

        self._prep_name_label()
        self.prep_state_label()

class WarriorNPC(NPC):
    pass
