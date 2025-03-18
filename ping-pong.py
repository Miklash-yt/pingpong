from pygame import *
window = display.set_mode((700, 500))
blue = (93, 173, 254)

display.set_caption('Пинг-Понг')
clock = time.Clock()
fps = 60
game = True
finish = False

class GameSprite(sprite.Sprite): #! Главный класс
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size1, player_size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): #? Класс игрока
    def update_l(self):
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 595:
            self.rect.y += self.speed
    def update_r(self):
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed

class Ball(GameSprite): #! класс мяча
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2, speed_y):
        super().__init__(player_image, player_x, player_y, player_speed, player_size1, player_size2)
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(racket, self) or sprite.collide_rect(racket2, self):
            self.speed *= -1

            


racket = Player('racket.png', 50, 250, 2, 50, 190)
racket2 = Player('racket.png', 620, 250, 2, 50, 190)
ball = Ball('ball.png', 350, 250, 2, 50, 50, 2)

font.init()
font1 = font.SysFont('Arial', 33)




while game:
    keys_pressed = key.get_pressed()
    if finish != True:
        window.fill(blue)
        racket.update_l()
        racket.reset()
        racket2.update_r()
        racket2.reset()
        ball.update()
        ball.reset()
        if ball.rect.x >= 690:
            finish = True
            lose = font1.render('ИГРОК 2 ПРОИГРАЛ:(', True, (255, 0, 0))
            window.blit(lose, (200, 200))
        if ball.rect.x <= 5:
            finish = True
            lose = font1.render('ИГРОК 1 ПРОИГРАЛ:(', True, (255, 0, 0))
            window.blit(lose, (200, 200))

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)
    