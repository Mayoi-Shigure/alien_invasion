#12.3.1　创建 Pygame 窗口及响应用户输入
import sys

import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """开始游戏的循环"""
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 让最近绘制的屏幕可见
            pygame.display.flip()
            
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
    
#12.3.2　控制帧率


#12.3.3　设置背景色


#12.3.4　创建 Settings 类


#12.4.2　在屏幕上绘制飞船


#12.5.1　_check_events() 方法


#12.5.2　_update_screen() 方法


#12.6.1　响应按键


#12.6.2　允许持续移动


#12.6.3　左右移动


#12.6.6　重构 _check_events()


#12.6.7　按 Q 键退出


#12.6.8　在全屏模式下运行游戏


#12.8.3　将子弹存储到编组中


#12.8.4　开火


#12.8.5　删除已消失的子弹


#12.8.6　限制子弹数量


#12.8.7　创建 _update_bullets() 方法