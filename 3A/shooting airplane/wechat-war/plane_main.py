import pygame as pg
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏的窗口
        self.screen = pg.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pg.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.create_sprites()
        # 4.设置定时器事件——重复创建
        pg.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 每隔1秒创建敌机
        pg.time.set_timer(HERO_FIRE_EVENT, 500) # 每隔0.5秒发射子弹
        self.is_alive = True # 游戏运行状态
        # 5.加载声音
        pg.mixer.init()
        pg.mixer.music.load("sound/game_music.ogg")
        pg.mixer.music.set_volume(0.2)
        self.bullet_sound = pg.mixer.Sound("sound/bullet.wav")
        self.bullet_sound.set_volume(0.2)
        self.enemy_down_sound = pg.mixer.Sound("sound/enemy1_down.wav")
        self.enemy_down_sound.set_volume(0.2)
        self.me_down_sound = pg.mixer.Sound("sound/me_down.wav")
        self.me_down_sound.set_volume(0.2)
        self.delay = 100  # 用于控制播放子弹声音的频率

    # 定义精灵和精灵组
    def create_sprites(self):
        # 创建背景精灵和精灵组
        self.bg1 = Background()
        self.bg2 = Background(True)
        self.bg_group = pg.sprite.Group(self.bg1, self.bg2)
        # 创建敌机的精灵组
        self.enemy_group = pg.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pg.sprite.Group(self.hero)
        # 爆炸效果图的精灵组
        self.explosion_group =  pg.sprite.Group()
        self.background = self.bg1.image.convert() 
        
    # 游戏循环
    def start_game(self):
        pg.init()
        pg.mixer.music.play(-1)  # -1:循环播放音乐
        
        self.hero.is_alive = True
        self.running = True
        while self.running:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.event_handler()
            # 3.碰撞检测
            self.check_collide()
            # 4.更新/绘制精灵组
            self.update_sprites()
            # 5.更新屏幕显示
            pg.display.update()
        
        # 6.游戏结束
        self.game_over()        

    # 游戏结束
    def game_over(self):
        print("游戏结束...")
        pg.time.self.delay(2000)
        #pg.time.wait(2000)
        pg.quit()
        exit()

    # 定义事件监听函数
    def event_handler(self):
        for event in pg.event.get():
            # 判断是否退出游戏
            if event.type == pg.QUIT:
                PlaneGame.game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:
                # 在设定的间隔时间重复创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        
        # 播放子弹声音
        if not(self.delay % 20):
            self.bullet_sound.play()
        self.delay -= 1
        if self.delay == 0: # 递减到0时， 恢复初始值
            self.delay = 100
        
        # 获取键盘按键
        keys_pressed = pg.key.get_pressed()
        # 控制英雄飞机移动
        if keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]:
            self.hero.rect.x += 2
        elif keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]:
            self.hero.rect.x -= 2
        elif keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]:
            self.hero.rect.y -= 2
        elif keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]:
            self.hero.rect.y += 2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def check_collide(self):
        # 1.子弹摧毁敌机—— groupcollide可以判断两个精灵组之间是否碰撞
        hits = pg.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        if hits:
            self.enemy_down_sound.play()
    
        # 第3，4个参数：dokilla, dokillb 
        # 都为True, 子弹和敌机都消失
        
        # 2.敌机撞毁英雄——spritecollide可以判断精灵和精灵组之间是否碰撞
        enemies = pg.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有碰撞
        if len(enemies) > 0:
            self.me_down_sound.play()
            for enemy in enemies:
                print('colliding with enemies！')
                self.hero.is_alive = False 
                #爆炸效果
                explosion1 = Explosion(self.hero) 
                explosion2 = Explosion(enemy) 
                self.explosion_group.add(explosion1)
                self.explosion_group.add(explosion2)
                gameover = Gameover() # 游戏结束文字
                self.explosion_group.add(gameover)
                
                self.running = False # 结束游戏
                
    # 刷新显示精灵
    def update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        
        self.explosion_group.update()
        self.explosion_group.draw(self.screen)
        
            
        ''' 放在这里看不到爆炸效果就结束了！
        if not self.hero.is_alive:
            #pg.time.wait(2000)
            self.explosion_group.update()
            self.explosion_group.draw(self.screen)
            pg.time.self.delay(1000)
            print('in update_sprites')
            self.screen.blit(self.background, (0, 0))  # 刷新背景
            # 文字提示
            gameover_font = pg.font.Font(None, 66)
            gameover_text = gameover_font.render("Game over!", True, (255, 0, 0))
            text_rect = gameover_text.get_rect()
            text_rect.topleft = [100, 200]
            self.screen.blit(gameover_text, text_rect)  
            
            pg.time.self.delay(1000)
            self.running = False
            
        '''
        '''   
        if not self.hero.is_alive:
            pg.time.wait(3000)
            self.game_over()
        '''


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()