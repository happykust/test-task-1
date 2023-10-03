class Animal:
    def __init__(self, is_tail: bool):
        self.is_tail = is_tail


dog = Animal(
    is_tail=True)

lol_player = Animal(is_tail=False)
print(dog.is_tail)
print(lol_player.is_tail)
lol_player.is_tail = True
print(f"New lol animal with tail: {lol_player.is_tail}")
