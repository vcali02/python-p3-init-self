#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

winnie = Dog("Winnie", "Poodle")
print(winnie.name)
print(winnie.breed)
