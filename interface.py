import random
import sys
import pygame
import resurse_pack
from resurse_pack import GameObject, result_game, restart, score

pygame.init()

window = pygame.display.set_mode((900, 600))
user_rock = GameObject(window, 'rock.png', 150, 415)
user_paper = GameObject(window, 'paper.png', 450, 415)
user_scissor = GameObject(window, 'scissor.png', 750, 415)
pc_scissor = GameObject(window, 'scissor.png', 150, 10)
pc_scissor.rotate()
pc_paper = GameObject(window, 'paper.png', 450, 10)
pc_paper.rotate()
pc_rock = GameObject(window, 'rock.png', 750, 10)
pc_rock.rotate()
pc_objects = [pc_rock, pc_scissor, pc_paper]
user_objects = [user_scissor, user_paper, user_rock]
result_game = result_game(window, 'won.png', 450, 50)
restart = restart(window, 'restart.png', 450, 500)
score = score(window, 'score.png', 450, 0)

def get_user_object():
    for object in user_objects:
        if object.is_show == True:
            return object

def get_pc_object():
    for object in pc_objects:
        if object.is_show == True:
            return object

def check_result():
    print(get_user_object(), get_pc_object())
    user_choice = get_user_object()
    pc_choice = get_pc_object()
    result_game.is_show = True
    restart.is_show = True
    if user_choice.hand == pc_choice.hand:
            result_game.image = pygame.image.load(result_game.img_drawn)
    elif user_choice.hand == 'paper':
        if pc_choice.hand == 'scissor':
            result_game.image = pygame.image.load(result_game.img_lost)
            score.add_pc_score()
        else:
            result_game.image = pygame.image.load(result_game.img_won)
            score.add_user_score()
    elif user_choice.hand == 'scissor':
        if pc_choice.hand == 'paper':
            result_game.image = pygame.image.load(result_game.img_won)
            score.add_user_score()
        else:
            result_game.image = pygame.image.load(result_game.img_lost)
            score.add_pc_score()
    else:
        if pc_choice.hand == 'paper':
            result_game.image = pygame.image.load(result_game.img_lost)
            score.add_pc_score()
        else:
            result_game.image = pygame.image.load(result_game.img_won)
            score.add_user_score()

def restart_game():
    user_rock.default_pos()
    user_scissor.default_pos()
    user_paper.default_pos()
    pc_rock.default_pos()
    pc_scissor.default_pos()
    pc_paper.default_pos()
    result_game.is_show = False
    restart.is_show = False

while True:
    window.fill((255, 255, 255))
    score.show()
    user_rock.actions(1, -1)
    user_paper.actions(0, -1)
    user_scissor.actions(-1, -1)
    pc_scissor.actions(1, 1)
    pc_paper.actions(0, 1)
    pc_rock.actions(-1, 1)
    result_game.draw()
    restart.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if resurse_pack.left_click(user_objects, pc_objects) and restart.is_show == False:
                    check_result()
                elif restart.rect.collidepoint(pygame.mouse.get_pos()) and restart.is_show == True:
                    restart_game()
    pygame.display.flip()