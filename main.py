from pygame import *

# ****************************** CLASESS ******************************



class GameSprite(sprite.Sprite):
    def __init__(self, filename_img, x, y, width, height, speed):
        
        sprite.Sprite.__init__(self)
        self.image = image.load(filename_img)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        if key.get_pressed()[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        elif key.get_pressed()[K_DOWN] and self.rect.y <= SIZE[1] - self.rect.height:
            self.rect.y += self.speed
    def update_l(self):
        if key.get_pressed()[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        elif key.get_pressed()[K_s] and self.rect.y <= SIZE[1] - self.rect.height:
            self.rect.y += self.speed

# ****************************** WINDOW ******************************

BACKGROUND = (0, 255, 255)
PURPLE = (255, 0, 255)

init()

SIZE = (500, 500)
window = display.set_mode(SIZE)


window.fill(BACKGROUND)
display.update()


player_1 = Player("data/player_1.png", 50, 50, 20, 75, 10)
player_2 = Player("data/player_2.png", SIZE[0] - 50 - 20, 50, 20, 75, 10)
ball = GameSprite("data/ball.png", 250, 250, 50, 50, 5)
ball_x = 2 
ball_y = 3


# ****************************** GAME LOOP ******************************

clock = time.Clock()
lost = False
state = True
while state:
    window.fill(BACKGROUND)
    player_1.reset()
    player_2.reset()
    ball.reset()

    for ev in event.get():
        if ev.type == QUIT:
            state = False

    if lost:
        font.init()
        lose = font.Font(None, 32)
        
        if ball.rect.x < 0:
            window.blit(lose.render("Left side lost", True, PURPLE), (250, 250))
        else:
            window.blit(lose.render("Right side lost", True, PURPLE), (250, 250)) 
        continue

    if sprite.collide_rect(ball, player_1) or sprite.collide_rect(ball, player_2) :
        ball_x *= (-1)
        ball_y *= (-1)

    if ball.rect.y <= 0 or ball.rect.y >= SIZE[1] - ball.rect.height:
        ball.rect.y *= (-1)


    if ball.rect.x < 0:
        lost = True
    elif ball.rect.x >= SIZE[1] - 30:
        lost = True

    player_1.update_l()
    player_2.update_r()

    ball.rect.x += ball_x
    ball.rect.y += ball_y

    display.update()
    clock.tick(60)