import random
import arcade


class Pear(arcade.Sprite):
    def __init__(self,game):
        super().__init__("my-project\session15\pear.png")
        self.width=30
        self.height=30
        self.center_x=random.randint(10, game.width-10)
        self.center_y=random.randint(10, game.height-10)

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("my-project\session15\Apple.png")
        self.width=30
        self.height=30
        self.center_x=random.randint(10, game.width-10)
        self.center_y=random.randint(10, game.height-10)

class Bomb(arcade.Sprite):
    def __init__(self,game):
        super().__init__("my-project\session15\Bomb.png")
        self.width=50
        self.height=50
        self.center_x=random.randint(10, game.width-10)
        self.center_y=random.randint(10, game.height-10)