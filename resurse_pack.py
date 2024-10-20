import pygame
import random

class basic_object():
    def __init__(self, window, img, x, y):
        self.screen = window
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.is_show = True

class result_game(basic_object):
    def __init__(self, window, img, x, y):
        super().__init__(window, img, x, y)
        self.is_show = False
        self.img_won = 'won.png'
        self.img_lost = 'lost.png'
        self.img_drawn = 'drawn.png'
    def draw(self):
        if self.is_show == True:
            self.screen.blit(self.image, self.rect)

class GameObject(basic_object):
    def __init__(self, window, img, x, y):
        super().__init__(window, img, x, y)
        self.is_move = False
        self.hand = img[:-4]
        print(self.hand)
        self.default_x = x
        self.default_y = y
        self.no_response = False

    def default_pos(self):
        self.rect.centerx = self.default_x
        self.rect.y = self.default_y
        self.is_show = True
        self.is_move = False
        self.no_response = False

    def actions(self, x, y):
        if self.is_show == True:
            self.screen.blit(self.image, self.rect)
        self.move(x, y)

    def rotate(self):
        rotate_img = pygame.transform.rotate(self.image, 180)
        self.image = rotate_img

    def move(self, x, y):
        speed = 4
        x = x*speed
        y = y*speed
        if self.is_move == False:
            return
        if self.rect.centery < 300 - speed or self.rect.centery > 300 + speed:
            self.rect.centery+=y
        else:
            if x == 0:
                self.is_move = False
        if self.rect.centerx < 450-speed or self.rect.centerx > 450+speed:
            self.rect.centerx+=x
        else:
            if x != 0:
                self.is_move = False

def left_click(my_objects, pc_objects):
    for object in my_objects:
        if object.rect.collidepoint(pygame.mouse.get_pos()) == True:
            if object.no_response == True:
                return False
            object.is_move = True
            object.no_response = True
            pc_object = random.choice(pc_objects)
            pc_object.is_move = True
            for object_for_hide in my_objects:
                if object_for_hide != object:
                    object_for_hide.is_show = False
            for pc_object_for_hide in pc_objects:
                if pc_object_for_hide != pc_object:
                    pc_object_for_hide.is_show = False
            return True
    return False

class restart(basic_object):
    def __init__(self, window, img, x, y):
        super().__init__(window, img, x, y)
        self.is_show = False
        self.img_restart = 'restart.png'
    def draw(self):
        if self.is_show == True:
            self.screen.blit(self.image, self.rect)

class score(basic_object):
    def __init__(self, window, img, x, y):
        super().__init__(window, img, x, y)
        self.user_wins = 0
        self.pc_wins = 0
        self.font = pygame.font.SysFont('Agency FB', 40)
        self.text_user_wins = self.font.render(f'{self.user_wins}', True, (0, 0, 0), (255, 255, 255))
        self.rect_text_user_wins = self.text_user_wins.get_rect()
        self.rect_text_user_wins.x = 100
        self.rect_text_user_wins.y = 300
        self.text_pc_wins = self.font.render(f'{self.pc_wins}', True, (0, 0, 0), (255, 255, 255))
        self.rect_text_pc_wins = self.text_pc_wins.get_rect()
        self.rect_text_pc_wins.x = 830
        self.rect_text_pc_wins.y = 300

    def add_user_score(self):
        self.user_wins += 1
        self.text_user_wins = self.font.render(f'{self.user_wins}', True, (0, 0, 0), (255, 255, 255))
        print(self.user_wins)

    def add_pc_score(self):
        self.pc_wins += 1
        self.text_pc_wins = self.font.render(f'{self.pc_wins}', True, (0, 0, 0), (255, 255, 255))
        print(self.pc_wins)

    def show(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text_user_wins, self.rect_text_user_wins)
        self.screen.blit(self.text_pc_wins, self.rect_text_pc_wins)
