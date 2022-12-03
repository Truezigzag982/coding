#import py
import pygame
import sys
import pygame.locals
import os
# 赛车双人游戏：屏幕滚动效果

WIDTH, HEIGHT = 350, 474  # 屏幕窗体大小
BG_SPEED = 1 # 背景滚动速度
vect = pygame.math.Vector2  # 二维向量

def load_image(file):
    """加载指定图片"""
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    #return surface.convert()
    return surface.convert_alpha()
 
 
# 4、创建图形(精灵类的子类)：
class Car(pygame.sprite.Sprite):
    def __init__(self, image, pos=(100, 80)):
        super().__init__()
        self.image = load_image(image)
        self.rect = self.image.get_rect()        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.width = self.rect.width
        self.height = self.rect.height
    

class Background(pygame.sprite.Sprite):
    """滚动背景"""
    def __init__(self, image, speed):  # speed是背景滚动速度
        super().__init__()
        #定义对象属性
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.speed = speed
        
    def update(self): # 刷新显示时会调用的方法
        self.rect.y += self.speed  #垂直向上移动
        #判断是否移出屏幕，若移出屏幕，应该将图像设置到图像上方
        if self.rect.y >= HEIGHT:
            self.rect.y = -self.rect.height
            

def start_game():
    # 1、初始化：
    pygame.init()  # Initialize 

    # 2、设置后续需用的变量或常量：
    FPS = 60  # 显示刷新：每秒帧数
    timer = pygame.time.Clock() # 用于刷新的时钟
    
    # 3、创建窗体：游戏屏幕
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("双打游戏：屏幕滚动")
    
    # 创建精灵对象
    redcar = Car("greencar.png",  (225, 350))
    bluecar = Car("bluecar.png", (70, 350))

    # 创建背景
    bg1 = Background("background-1_0 copy.png", BG_SPEED)
    bg2 = Background("background-1_0.png", BG_SPEED)
    bg2.rect.y = -bg2.rect.height
    # 2张背景图交替出现
    
    # 添加精灵对象到精灵组
    group = pygame.sprite.Group()
    group.add(bg1)
    group.add(bg2)
    group.add(redcar)
    group.add(bluecar)
        
    VEL = 2   # 车移动速度
    
    # 键盘控制蓝车移动
    def blue_handle_movement(keys_pressed, blue):
        if keys_pressed[pygame.K_a] and blue.rect.x - VEL > 70:  # LEFT
            blue.rect.x -= VEL
        if keys_pressed[pygame.K_d] and blue.rect.x + VEL + blue.width < WIDTH//2 + 20:  # RIGHT，不过中线
            blue.rect.x += VEL
        if keys_pressed[pygame.K_w] and blue.rect.y - VEL > 0:  # UP
            blue.rect.y -= VEL
        if keys_pressed[pygame.K_s] and blue.rect.y + VEL + blue.height < HEIGHT - 15:  # DOWN
            blue.rect.y += VEL

    # 键盘控制红车移动
    def red_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.rect.x - VEL > WIDTH//2 - 20:  # LEFT ，不过中线
            red.rect.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.rect.x + VEL + red.width < WIDTH - 70:  # RIGHT
            red.rect.x += VEL
        if keys_pressed[pygame.K_UP] and red.rect.y - VEL > 0:  # UP
            red.rect.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.rect.y + VEL + red.height < HEIGHT - 15:  # DOWN
            red.rect.y += VEL
            
    # 游戏循环：
    while True:
        for event in pygame.event.get():
            # 退出游戏程序
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit() 
            
        # 键盘事件控制精灵移动：    
        keys_pressed = pygame.key.get_pressed()
        blue_handle_movement(keys_pressed, bluecar)
        red_handle_movement(keys_pressed, redcar)
        
        group.update()
        group.draw(screen)
        timer.tick(FPS)  # 刷新帧数
        pygame.display.flip() # 刷新显示整个屏幕
        
if __name__ == '__main__':
    start_game()