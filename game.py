#12.3.1　创建 Pygame 窗口及响应用户输入
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        # 设置背景色
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """开始游戏的循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        # 侦听键盘和鼠标事件
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)       
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """响应按下"""       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True        
        elif event.key == pygame.K_q:
            sys.exit()            
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()          
                    
    def _check_keyup_events(self, event):
        """响应释放"""                
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False            
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组 bullets """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
            
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)    
                    
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
            
        pygame.display.flip()
            
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
    
#12.3.2　控制帧率 √

#12.3.3　设置背景色 √

#12.3.4　创建 Settings 类 √

#12.4.1　创建 Ship 类 √

#12.4.2　在屏幕上绘制飞船 √

#12.5.1　_check_events() 方法 √

#12.5.2　_update_screen() 方法 √

#12.6.1　响应按键 √

#12.6.2　允许持续移动 √

#12.6.3　左右移动 √

#12.6.4　调整飞船的速度 √

#12.6.5　限制飞船的活动范围 √

#12.6.6　重构 _check_events() √

#12.6.7　按 Q 键退出 √

#12.6.8　在全屏模式下运行游戏 √

#12.8.1　添加子弹设置 √

#12.8.2　创建 Bullet 类 √

#12.8.3　将子弹存储到编组中 √

#12.8.4　开火 √

#12.8.5　删除已消失的子弹 √

#12.8.6　限制子弹数量 √

#12.8.7　创建 _update_bullets() 方法 √