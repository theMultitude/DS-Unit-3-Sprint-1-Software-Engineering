#!/usr/bin/env python
"""Acme classes to represent inventory items."""

from random import randint

class Product:
    
    """Base Acme Product class."""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def stealability(self):
        """Calculate and return how stealable an item is."""
        value_weight_ratio = self.price / self.weight
        if value_weight_ratio < 0.5:
            return 'Not so stealable...'
        elif value_weight_ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    def explode(self):
        """Make the item go boom!"""
        potency = self.flammability * self.weight
        if potency < 10:
            return '...fizzle.'
        elif potency < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    
    """The Acme Box-o-Matic!"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """The main purpose of a boxing glove."""
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"