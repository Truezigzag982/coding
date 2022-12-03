import random
import pygame as pg
import os

# 当前python文件所在目录
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    """加载图片：loads an image, prepares it for play"""
    file = os.path.join(main_dir, "images", file) # 资源文件在..\images文件夹下
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

# 定义屏幕大小的常量
SCREEN_RECT = pg.Rect(0, 0, 480, 700)
# 定义刷新帧率的常量
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pg.USEREVENT
# 英雄发射子弹事件常量
HERO_FIRE_EVENT = pg.USEREVENT + 1


class GameSprite(pg.sprite.Sprite):
    """飞机大战游戏精灵：父类"""
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pg.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed # 设置精灵初始速度

    def update(self):
        # 在屏幕的垂直方向移动 (speed为正数时向下，为负数时向上)
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵, 继承父类"""
    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        if is_alt:  # 背景滚动
            self.rect.y = -self.rect.height

    def update(self):
        super().update() # 1.调用父类的方法，实现向下移动
        # 2.重写父类方法，实现屏幕滚动效果
        # 如果移出屏幕下方，将图像移至屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵, 继承父类"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度——1到3
        self.speed = random.randint(1, 3)
        self.is_alive = True
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0  # 设置敌机是从屏幕外飞进屏幕
        # 敌机要完整的在屏幕内 — 敌机的最大X值是屏幕的宽减去敌机的宽
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是 需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height or not self.is_alive:  
            # 敌机的y值大于屏幕的高即飞出屏幕，或者当敌机碰撞到我机时
            # print("飞出屏幕，需从精灵组中删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵自动销毁
            self.kill()


class Hero(GameSprite):
    """英雄精灵：玩家飞机"""
    def __init__(self):
        # 1.调用父类方法设置image和速度
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pg.sprite.Group()
        self.is_alive = True

    def update(self):
        # 改写父类方法，不会向下移动
        # 控制英雄不能离开屏幕
        if self.is_alive:
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.right > SCREEN_RECT.width:
                self.rect.right = SCREEN_RECT.width
            elif self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.bottom > SCREEN_RECT.bottom:
                self.rect.bottom = SCREEN_RECT.bottom
        else:
            self.kill()
            pass
            
    def fire(self):
        """发射子弹"""
        if self.is_alive:
            for i in range(3):  # 三连发
                # 1.创建子弹精灵
                bullet = Bullet()
                # 2.设置子弹的位置，在飞机上方
                bullet.rect.bottom = self.rect.y - i * 20
                bullet.rect.centerx = self.rect.centerx
                # 3.将子弹精灵添加到精灵组
                self.bullets.add(bullet)
            

class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法设置子弹图片和初始速度-2（就是向上运动）
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用方法让子弹沿垂直方向飞行
        super().update()

        # 子弹飞出上方屏幕就删除
        if self.rect.bottom < 0:
            self.kill()

class Gameover(GameSprite):
    """游戏结束精灵"""
    def __init__(self):
        super().__init__("./images/gameover.gif", 0)  # 速度为0，不移动


# Jet adds
class Explosion(pg.sprite.Sprite):
    """爆炸动画效果"""
    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pg.sprite.Sprite.__init__(self)
        img = load_image("explosion1.gif")
        self.images = [img, pg.transform.flip(img, 1, 1)]  # 水平和垂直翻转图片 
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        """ 爆炸动画效果 """
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2] 
        if self.life <= 0:
            self.kill()  # 相当于Scratch中的“删除克隆体”