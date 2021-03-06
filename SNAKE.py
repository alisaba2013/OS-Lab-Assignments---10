import random
import arcade

WIDTH = 600
HEIGHT = 500
SIZE = 6

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = SIZE
        self.height = SIZE
        self.body_pos_size = 0
        self.speed = 6
        self.color = arcade.color.BLACK
        self.body_pos = []

        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        
        self.change_x = 0
        self.change_y = 0
        
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_outline(self.center_x,self.center_y,self.width,self.height,arcade.color.WHITE,border_width=5,tilt_angle=45)

        for i , pos in enumerate(self.body_pos):
            if i%2 == 0:
                arcade.draw_rectangle_filled(pos[0],pos[1],self.width,self.height,self.color)

    def move(self):
        self.body_pos.append([self.center_x,self.center_y])

        if len(self.body_pos) > self.body_pos_size:
            self.body_pos.pop(0)


        if self.change_x == -1:
            self.center_x -= self.speed
        elif self.change_x == 1:
            self.center_x += self.speed
        
        if self.change_y == -1:
            self.center_y -= self.speed
        elif self.change_y == 1:
            self.center_y += self.speed

    def eat_apple(self):
        self.body_pos_size += 1
        self.score += 1
        self.app_music = arcade.load_sound(":resources:sounds/hit4.wav")
        arcade.play_sound(self.app_music)

    def eat_bahbah(self):
        self.score += 2
        self.bah_music = arcade.load_sound(":resources:sounds/hurt4.wav")
        arcade.play_sound(self.bah_music)

    def eat_ahah(self):
        self.score -= 1
        self.ah_music = arcade.load_sound(":resources:sounds/gameover2.wav")
        arcade.play_sound(self.ah_music)

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*4
        self.height = SIZE*4
        self.radius = 8
        self.color = arcade.color.RED
        
        self.center_x = random.randint(100,WIDTH-25)
        self.center_y = random.randint(100,HEIGHT-25)
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,self.color)

class Bahbah(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*3
        self.height = SIZE*3
        self.radius = 5
        self.color = arcade.color.YELLOW
        
        self.center_x = random.randint(50,WIDTH-100)
        self.center_y = random.randint(50,HEIGHT-100)
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,self.color)

class Ahah(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*3
        self.height = SIZE*3
        self.color = arcade.color.BROWN

        self.center_x = random.randint(25,WIDTH-75)
        self.center_y = random.randint(25,HEIGHT-75)

            
    def draw(self):
        arcade.draw_rectangle_outline(self.center_x,self.center_y,self.width,self.height,self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,title="SNAKE GAME",resizable=True)
        arcade.set_background_color(arcade.color.GREEN)
        
        self.snake = Snake()
        self.apple = Apple()
        self.bahbah = Bahbah()
        self.ahah = Ahah()

        self.over = 1

    def on_draw(self):
        arcade.start_render()
        
        if (self.snake.center_x < 0) or (self.snake.center_x > WIDTH) or (self.snake.center_y < 0) or (self.snake.center_y > HEIGHT):
            self.over = 0
            self.over_music = arcade.load_sound(":resources:sounds/gameover3.wav")
            arcade.play_sound(self.over_music)       
            arcade.pause(0.5)

        if self.over > 0:
            arcade.draw_text("RED : + / Yellow : ++ / Brown : --",200,480,arcade.color.BLACK,width=600,font_size=10)
            
            text = f"score : {self.snake.score}"
            arcade.draw_text(text,250,5,arcade.color.BLACK,15)

            self.snake.draw()
            self.apple.draw()
            self.bahbah.draw()
            self.ahah.draw()
        else:
            arcade.draw_text("GAME OVER!",0,250,arcade.color.WHITE,width=600,font_size=15,align='center')
            text = f"score : {self.snake.score}"
            arcade.draw_text(text,250,50,arcade.color.BLACK,15)    
        

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat_apple()
            self.apple = Apple()

        elif arcade.check_for_collision(self.snake,self.bahbah):
            self.snake.eat_bahbah()
            self.bahbah = Bahbah()

        elif arcade.check_for_collision(self.snake,self.ahah):
            self.snake.eat_ahah()
            self.ahah = Ahah()

    def on_key_press(self, key: int, modifiers: int):  
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN:
            self.snake.change_y = -1
            self.snake.change_x = 0
    
snake_game = Game()
snake_game.center_window()
arcade.run()
