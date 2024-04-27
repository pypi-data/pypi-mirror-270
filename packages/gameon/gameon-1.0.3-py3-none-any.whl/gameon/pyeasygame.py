import pygame
import random as r
import keyboard as kb
import sys
import time as t
import os

pygame.init()
pygame.display.set_caption('PyEasyGame Window')

package_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the icon image relative to the package directory
icon_path = os.path.join(package_dir, 'logo.ico')

icon_img = pygame.image.load(icon_path)

pygame.display.set_icon(icon_img)

#window variables
screen = None
screen_once = True
screen_color = (255,255,255)
screen_width = 0
screen_height = 0

#time variables
clock = pygame.time.Clock()

#variables
frames = 60
time = 0 #time delay

#player
player_x = 0
player_y = 0
jumped = False
jump_velocity = 0
player_width = 0
player_height = 0
player_run_once = True
player_speed = 0
original_x = 0
original_y = 0
change_x = 0
change_y = 0

#mouse_click
left_click = False
right_click = False

#key_pressed
keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space','1','2','3','4','5','6','7','8','9','0']
pygame_keys = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z,pygame.K_SPACE,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_0]
keys_boolean = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def box(image,x,y,rect,collision=True):
    global player_x,player_y,player_width,player_height,player_speed
    player_rect = pygame.Rect(rect)
    col_box = pygame.Rect(x,y,image.get_width(),image.get_height())
    if collision:
        if player_rect.colliderect(col_box):
            if player_rect.right >= col_box.x and player_rect.right <= col_box.x + (player_speed + 2) :
                player_x = col_box.x - player_rect.width
            if player_rect.left >= col_box.right - (player_speed + 2) and player_rect.left <= col_box.right:
                player_x = col_box.right
            if player_rect.top <= col_box.bottom and player_rect.top >= col_box.bottom - (player_speed + 2):
                player_y = col_box.bottom
            if player_rect.bottom >= col_box.top and player_rect.bottom <= col_box.top + (player_speed + 2):
                player_y = col_box.top - player_rect.height
    screen.blit(image, (x,y))
    pass

def collide(rect1,rect2):
    player_rect = pygame.Rect(player_x,player_y,player_width,player_height)
    mouse_pos = pygame.mouse.get_pos()
    if rect1 == 'player':
        if rect2 != 'mouse':
            if pygame.Rect(player_rect).colliderect(pygame.Rect(rect2)):
                return True
        if rect2 == 'mouse':
            if pygame.Rect(player_rect).collidepoint(mouse_pos):
                return True
    if rect2 == 'player':
        if rect1 != 'mouse':
            if pygame.Rect(player_rect).colliderect(pygame.Rect(rect2)):
                return True
        if rect1 == 'mouse':
            if pygame.Rect(player_rect).collidepoint(mouse_pos):
                return True
    if rect1 == 'mouse':
        if rect2 != 'player':
            if pygame.Rect(rect2).collidepoint(mouse_pos):
                return True
        if rect2 == 'player':
            if pygame.Rect(player_rect).collidepoint(mouse_pos):
                return True
    if rect2 == 'mouse':
        if rect1 != 'player':
            if pygame.Rect(rect2).collidepoint(mouse_pos):
                return True
        if rect1 == 'player':
            if pygame.Rect(player_rect).collidepoint(mouse_pos):
                return True
    if not isinstance(rect1,str) and not isinstance(rect2,str):
        if pygame.Rect(rect1).colliderect(pygame.Rect(rect2)):
            return True
    pass


class Lives:
    def __init__(self,full_heart_img, empty_heart_img, x,y,lives,draw_lives=True):
        self.img1 = full_heart_img
        self.img2 = empty_heart_img
        self.x = x
        self.y = y
        self.health = lives
        self.draw_lives = draw_lives
        pass
    def draw(self,current_lives):
        self.current_lives = current_lives
        if self.draw_lives:
            for i in range(self.health):
                screen.blit(self.img2,(self.x + self.img2.get_width() * i ,self.y))
            for i in range(self.current_lives):
                screen.blit(self.img1, (self.x + self.img1.get_width() * i,self.y))
            if self.current_lives <= 0:
                self.current_lives = 0
    def __int__(self):
        return self.current_lives
    pass

class Bar:
    def __init__(self,x,y,width,height,health,health_color,background_color=(255,0,0),border_radius=5, show=True):
        self.x = x
        self.y = y
        self.h = height
        self.color = health_color
        self.bg_color = background_color
        self.w = width
        self.health = health
        self.draw_bar = show
        self.border_radius = border_radius
        self.draw()
    def draw(self,current_health):
        self.current_health = current_health
        if self.draw_bar:
            pygame.draw.rect(screen, self.bg_color, (self.x,self.y,self.w,self.h))
            pygame.draw.rect(screen, self.color, (self.x,self.y,(self.w * self.current_health) / self.health ,self.h))
            pygame.draw.rect(screen, (0,0,0), (self.x,self.y,self.w,self.h), self.border_radius)
        if self.current_health <= 0:
            self.current_health = 0
        pass
    def __int__(self):
        return self.current_health
        pass
    pass