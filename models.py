from random import random


class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        pass


class Player:
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        pass



