# 面向对象编程模拟飞机大战（原型设计）
# 参考: https://www.youtube.com/watch?v=33g62PpFwsE
# 碰撞：Collisions and bullets
import pygame
import random

# 定义常量
WIDTH = 480
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 初始化游戏
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("碰撞")
clock = pygame.time.Clock()


class Mob(pygame.sprite.Sprite):
    """ 敌机 """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # 超过屏幕边界就重新显示
        if self.rect.top > HEIGHT + 10 or \
            self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Player(pygame.sprite.Sprite):
    """ 我方战机 """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        # 键盘控制左右运动
        # TODO： 增加上下运动
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
     

class Bullet(pygame.sprite.Sprite):
    """子弹"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # 离开屏幕就删除
        if self.rect.bottom < 0:
            self.kill()


def start_game():
    """游戏主程序""" 
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8): # 生成8架敌机
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    def shoot(player):
        """在我机中心位置上方发射子弹"""
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    score = 0
    def show_score(score):
        score_font = pygame.font.Font(None, 26)
        score_text = score_font.render((f'Score:{score}'), True, (0, 0, 255))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 20]
        screen.blit(score_text, text_rect)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # 按下空格键发射子弹
                    shoot(player)

        all_sprites.update() # 刷新显示所有精灵对象

        # 碰撞检测：敌方碰到子弹
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

        # 消灭敌机之后，创建同样多的新的敌机
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            score += 100
        
        # 碰撞检测：敌机（机群）碰到我方
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            running = False  # 终止游戏

        # 绘制、刷新显示
        screen.fill(BLACK)
        all_sprites.draw(screen)
        show_score(score)


        pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    start_game()