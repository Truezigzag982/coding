import pygame
import sys
import pygame.locals
import os
# 事件处理：用键盘控制精灵运动

# 1、初始化：
pygame.init()  # Initialize 
# 2、设置后续需用的变量或常量：
FPS = 30  # 显示刷新：每秒帧数
timer = pygame.time.Clock() # 用于刷新的时钟
# 3、创建窗体：游戏屏幕
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("双打游戏：控制车移动")

def load_image(file):
    """加载指定图片"""
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' 
                         % (file, pygame.get_error()))
    return surface.convert()
 
# 4、创建图形(精灵类的子类)：
class Car(pygame.sprite.Sprite):
    def __init__(self, image, pos=(100, 80)):
        # image: 赛车的图片,每个实例对象可以用不同图片
        super().__init__()
        self.image = load_image(image)
        self.rect = self.image.get_rect()        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.width = self.rect.width
        self.height = self.rect.height
    
'''
# 画出背景和车
def draw_screen(ground, cars_group, redcar, bluecar):
    screen.blit(ground, (0, 0)) # 画背景
    # 方法一：用精灵组画精灵
    #cars_group.update()
    #cars_group.draw(screen)
    
    # 方法二：逐个画精灵
    screen.blit(redcar.image, (redcar.rect.x, redcar.rect.y)) # 画精灵
    screen.blit(bluecar.image, (bluecar.rect.x, bluecar.rect.y)) # 画精灵
'''    
# 键盘控制蓝车移动
VEL = 2   # 移动速度
def blue_handle_movement(keys_pressed, blue):
    if keys_pressed[pygame.K_a] and blue.rect.x - VEL > WIDTH//2 + 10:  # LEFT ，不过中线
        blue.rect.x -= VEL
    if keys_pressed[pygame.K_d] and blue.rect.x + VEL + blue.width < WIDTH:  # RIGHT
        blue.rect.x += VEL
    if keys_pressed[pygame.K_w] and blue.rect.y - VEL > 0:  # UP
        blue.rect.y -= VEL
    if keys_pressed[pygame.K_s] and blue.rect.y + VEL + blue.height < HEIGHT - 15:  # DOWN
        blue.rect.y += VEL

# 键盘控制红车移动
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.rect.x - VEL > 0:  # LEFT
        red.rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.rect.x + VEL + red.width < WIDTH//2:  # RIGHT，不过中线
        red.rect.x += VEL
    if keys_pressed[pygame.K_UP] and red.rect.y - VEL > 0:  # UP
        red.rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.rect.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.rect.y += VEL

def main():
    # 创建精灵对象
    redcar = Car("greencar.png", (150, 200))
    bluecar = Car("bluecar.png", (300, 200))
    # 添加精灵对象到精灵组
    cars_group = pygame.sprite.Group()
    cars_group.add(redcar)
    cars_group.add(bluecar)

    # 创建背景
    bg_surface = load_image("background.png")
    ground = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT)) # 背景

    # 游戏循环：
    while True:
        for event in pygame.event.get():
            # 退出游戏程序
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit() 
        
        screen.blit(ground, (0, 0)) # 画背景
            
        # 键盘事件控制精灵移动：    
        keys_pressed = pygame.key.get_pressed()
        blue_handle_movement(keys_pressed, bluecar)
        red_handle_movement(keys_pressed, redcar)
        
        #draw_screen(ground, cars_group, redcar, bluecar) # 画出背景和精灵
        cars_group.update()
        cars_group.draw(screen)  # 把精灵组中所有精灵画到指定屏幕区中

        timer.tick(FPS)  # 刷新帧数
        pygame.display.flip() # 刷新显示整个屏幕
        
if __name__ == '__main__':
    main()