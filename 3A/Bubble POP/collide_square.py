import pygame
import sys
from pygame.locals import *
from random import *
# 精灵碰撞检测：气泡碰撞

class Bubble(pygame.sprite.Sprite):
    """气泡 """
    def __init__(self, image, position, speed, bg_size):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        # 左上角坐标
        self.rect.left, self.rect.top = position  
        self.position = position
        self.speed = speed
        # 背景屏幕的宽度、高度
        self.width, self.height = bg_size[0], bg_size[1]  
        self.image.fill("blue")    # 填充矩形，矩形碰撞时使用
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        # 遇到屏幕边缘就反弹
        if self.rect.right > self.width or self.rect.left < 0:
            self.speed[0] = -self.speed[0] # 左右反弹 
        if self.rect.bottom > self.height or self.rect.top < 0:
            self.speed[1] = -self.speed[1] # 上下反弹 

    def update(self):
        self.move()


def main():
    pygame.init()
    Bubble_image = "bubble.png"  # 气泡图
    bg_image = "background.png" # 背景图
    #根据背景图片设置游戏界面的尺寸
    bg_size = width, height = 1017, 637
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("气泡碰撞")
    background = pygame.image.load(bg_image).convert_alpha()
    group = pygame.sprite.Group()
    pygame.mixer.init()    # 声音初始化
    pop = pygame.mixer.Sound("pop.wav")  # 碰撞时的声音

    # 创建五个气泡：位置随机，速度随机
    for i in range(5):
        # 球的大小是 100 x 100 防止越出边界，所以要宽和高减 100 的范围以内
        position = randint(60, width - 100), randint(60, height - 100)
        speed = [randint(-5, 5), randint(-5, 5)] # 随机速度
        # 创建气泡对象
        bubble = Bubble(Bubble_image, position, speed, bg_size)
        
        # 创建气泡时需要检测，避免球与球之间发生重叠
        while pygame.sprite.spritecollide(bubble, group, False):
        #while pygame.sprite.spritecollide(bubble, group, False,
        #                                  pygame.sprite.collide_circle):
            # 若发生碰撞即有重叠，就重新设置位置
            bubble.rect.left = randint(0, width - 100)
            bubble.rect.top = randint(0, height - 100)
        group.add(bubble)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))  # 画背景

        for each in group:
            # 检测组中每一个气泡运动过程中是否发生碰撞
            # 先将其弹出，检测完后再加入
            group.remove(each)
            # 默认是矩形碰撞， 观察碰撞的效果（精灵不消失）
            b_collides = pygame.sprite.spritecollide(each, group, False) 
            # 默认是矩形碰撞， 观察碰撞的效果（精灵消失）
            # b_collides = pygame.sprite.spritecollide(each, group, True) 
            # 圆形碰撞，精灵不消失
            #b_collides = pygame.sprite.spritecollide(each, group, False,
            #                               pygame.sprite.collide_circle)
            if b_collides:
                pop.play() # 播放碰撞声音
                # 运动方向反向（反弹）
                each.speed[0] = -each.speed[0]  
                each.speed[1] = -each.speed[1]
            group.add(each)
        group.update()
        group.draw(screen)
        pygame.display.flip()
        clock.tick(30)  # 刷新帧数 30 次/秒

if __name__ == '__main__':
    main()
