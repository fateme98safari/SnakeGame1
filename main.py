import random
import arcade
from apple import Apple
from apple import Pear
from apple import Bomb
from snake import Snake

        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500 , height=500 , title="Snake Game")
        arcade.set_background_color(arcade.color.GREEN)
        self.apple=Apple(self)
        self.pear=Pear(self)
        self.bomb=Bomb(self)
        self.snake=Snake(self)
        self.game_status=" "
        
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.bomb.draw()
        self.snake.draw()
        arcade.draw_text("score: ",10,470,arcade.color.RED , 17,20)
        arcade.draw_text(self.snake.score , 80,470 ,arcade.color.RED , 15 , 20)
        if self.game_status=="game over":
            self.clear()
            arcade.draw_text("GAME OVER ",40,230,arcade.color.RED , 50,50)

        arcade.finish_render()


    def on_update(self, delta_time: float):
        self.snake.move()
        if self.snake.center_x ==500 or self.snake.center_x==0 or self.snake.center_y==500 or self.snake.center_y==0:
            self.game_status="game over" 

        for part in self.snake.body:
             if self.snake.center_x+30==part['x'] or self.snake.center_x+30==part['x'] or self.snake.center_y+30 ==part['y'] or self.snake.center_y-30==part['y']:
                self.game_status="game over"

        if arcade.check_for_collision(self.snake , self.apple):
            arcade.play_sound(self.snake.laser_sound)
            del self.apple
            self.snake.score +=1
            self.apple=Apple(self)

        elif arcade.check_for_collision(self.snake , self.pear):
            
            arcade.play_sound(self.snake.laser_sound)
            del self.pear
            self.snake.score +=2
            self.pear=Pear(self)
          
        elif arcade.check_for_collision(self.snake , self.bomb):
            arcade.play_sound(self.snake.laser_sound)
            if self.snake.score > 0:
                del self.bomb
                self.snake.score -=1
                self.bomb=Bomb(self)
            if self.snake.score == 0:
                self.game_status="game over"
            


    def on_key_release(self, symbol: int, modifiers: int):
        
        if symbol==arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y = -1
        elif symbol==arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y=0
        elif symbol==arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake_change_y = 0
   
    

game=Game()
arcade.run()
        


