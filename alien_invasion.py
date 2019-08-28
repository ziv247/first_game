import pygame
import sys
from setting import Setting
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_setting, screen, "Play")
    stats = GameStats(ai_setting)
    ship = Ship(screen, ai_setting)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, ship,aliens, bullets)
        # if stats.game_active:
        ship.update()
        gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
        gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_setting, screen, stats, ship, aliens, bullets, play_button)


run_game()
