from pygame import*

back = (200,255,255)
win_width = 500
win_height = 600
winndow = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = size_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= self.speed:
            if not keys[K_RIGHT]:
                self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x <= win_width - (self.width + self.speed):
            self.rect.x += self.speed
        

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

while Game:
    for e in event.get:
        if e.type = QUIT:
            game = False

    display.update()
    clock.tick(fps)
