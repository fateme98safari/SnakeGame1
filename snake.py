import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=30
        self.height=30
        self.center_x= game.width //2
        self.center_y= game.height//2
        self.color=arcade.color.BROWN
        self.change_x=0
        self.change_y=0
        self.speed=2
        self.score=0
        self.body=[]
        self.laser_sound = arcade.load_sound("my-project\session15\Guts-A2-med-www.fesliyanstudios.com.mp3")


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color) 
        for i in range (1,len(self.body)):
                if i%2==0:
                    arcade.draw_rectangle_filled(self.body[i]['x'] , self.body[i]['y'] , self.width , self.height, arcade.color.YELLOW)
                elif i%2 !=0:
                    arcade.draw_rectangle_filled(self.body[i]['x'] , self.body[i]['y'] , self.width , self.height, arcade.color.PURPLE)

    def move(self):
        self.body.append({'x': self.center_x,'y':self.center_y})
        if len(self.body)>self.score:
            self.body.pop(0)
            
        self.center_x +=self.change_x * self.speed
        self.center_y +=self.change_y * self.speed

        
