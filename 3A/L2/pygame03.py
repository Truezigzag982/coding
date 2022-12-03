# 为了避免找不到car.png文件，需要在VSCode中设置：
# File > Preferences > Settings > Extensions > Python > Terminal: Execute In File Dir.
# 文件->首选项->设置->输入Python(或在扩展中点击Python)->勾选：Python>Terminal:Execute in File Dir
import pygame
import sys
import pygame.locals

# 1、初始化：
pygame.init()  # Initialize 
# 2、设置后续需用的变量或常量：
FPS = 30  # 显示刷新：每秒帧数
timer = pygame.time.Clock() # 用于刷新的时钟
# 3、创建窗体：游戏屏幕
screen = pygame.display.set_mode((400, 300)) 
pygame.display.set_caption("创建游戏精灵") # 标题
 
# 4、创建精灵子类：
class Car(pygame.sprite.Sprite):
    def __init__(self, pos=(100, 80)):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.image = pygame.image.load("greencar.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]        
    

# 5、创建精灵对象，添加到精灵组中
car1 = Car()
car2 = Car((200, 180))
sprite_group = pygame.sprite.Group()
sprite_group.add(car1)
sprite_group.add(car2)

# 游戏循环：
while True:
    for event in pygame.event.get():
        # 退出游戏程序
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit() 
        
    timer.tick(FPS)  # 刷新帧数
    screen.fill(color='white')  # 为窗口填充白色
    sprite_group.update()
    sprite_group.draw(screen)  # 把精灵组中所有精灵画到指定屏幕区中
    pygame.display.flip() # 刷新显示整个屏幕
    