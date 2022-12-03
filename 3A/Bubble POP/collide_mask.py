import pygame
import random
# https://blog.csdn.net/BAIFOL/article/details/121542052
# pygame.mask实现精准碰撞检测
# 请用鼠标带动红色圆点与其它颜色圆点碰撞，看会发生什么变化

class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, color, *grps):  #*args表示有多个(个数不定)无名参数
        super().__init__(*grps)
        self.color = color
        self.image = pygame.Surface((32, 32))  #创建1个32X32的Surface实例image
        self.image.set_colorkey((0, 0, 0))  #设置image中指定颜色为透明色
        self.image.fill((0, 0, 0))  #底色为黑色，由于上条，底色变为透明
        self.radius = 15
        pygame.draw.circle(self.image, 
                           pygame.Color(self.color), 
                           (15, 15), self.radius)  #在image上画圆
        self.rect = self.image.get_rect(center=pos)  #将image移到指定位置
        self.mask = pygame.mask.from_surface(self.image)

    
def main():        
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("两圆相碰改变背景色")
    clock = pygame.time.Clock()
    colors = ['green', 'yellow', 'purple', 'blue']
    objects = pygame.sprite.Group()

    for n in range(10):  #创建10个圆，位置随机但固定不变，颜色随机
        pos = random.randint(20, 380), random.randint(20, 280)
        Circle(pos, random.choice(colors), objects)  #创建Circle实例并增加到列表objects
    player = Circle(pygame.mouse.get_pos(), 'red')  #创建1个圆，将随鼠标移动和10个圆发生碰撞

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        player.rect.center = pygame.mouse.get_pos()  # player随鼠标移动
        # 从objects中获取和player碰撞的sprite
        aSprite = pygame.sprite.spritecollideany(
            player, objects, pygame.sprite.collide_mask)  #无碰撞为None
        if aSprite:  #如发生碰撞，背景变为被碰撞圆的颜色，碰撞圆的颜色和背景同色，将看不见
            screen.fill(pygame.Color(aSprite.color))
        else:
            screen.fill('white')  #无碰撞背景色是白色
        objects.update()
        objects.draw(screen)
        screen.blit(player.image, player.rect)
        clock.tick(10)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()