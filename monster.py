import pygame
import random
import math

class Monster(object):
    def __init__(self, sprite):
        self.x_dir = 5
        self.y_dir = 5
        self.x = 350
        self.y = 375
        self.alive = True
        self.monster_image = \
        pygame.image.load(sprite).convert_alpha()

class Hero(object):
    def __init__(self):
        self.x_dir = 5
        self.y_dir = 5
        self.x = 255
        self.y = 240

        self.hero_image = \
        pygame.image.load('images/hero.png').convert_alpha()

def main():
    width = 510
    height = 480

    blue_color = (97, 159, 182)

    #sound stuff
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/win.wav')

    #screen stuff
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

    #clock
    clock = pygame.time.Clock()

    # Game initialization

    pygame.key.set_repeat(1, 100)
    change_dir_countdown = 120
    pygame.init()

    #font stuff
    font = pygame.font.SysFont('arial', 40)
    text = font.render('You won! Hit ENTER to play again', 1, (255, 0, 0))

    monster = Monster('images/monster.png')
    hero = Hero()

    stop_game = False

    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print "hello"
                if event.key == 273:
                    hero.x_dir = 0
                    hero.y_dir = -10
                    hero.x += hero.x_dir
                    hero.y += hero.y_dir
                elif event.key == 274:
                    hero.x_dir = 0
                    hero.y_dir = 10
                    hero.x += hero.x_dir
                    hero.y += hero.y_dir
                elif event.key == 276:
                    hero.x_dir = -10
                    hero.y_dir = 0
                    hero.x += hero.x_dir
                    hero.y += hero.y_dir
                elif event.key == 275:
                    hero.x_dir = 10
                    hero.y_dir = 0
                    hero.x += hero.x_dir
                    hero.y += hero.y_dir

            if hero.x > 478:
                hero.x = 478
            if hero.x < 10:
                hero.x = 10
            if hero.y > 448:
                hero.y = 448
            if hero.y < 10:
                hero.y = 10

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        if monster.alive == True:
            change_dir_countdown -= 1

            if change_dir_countdown == 0:
                change_dir_countdown = 10
                z = random.randint(0,7)
                if z == 0:
                    monster.x_dir = 0
                    monster.y_dir = -5
                if z == 1:
                    monster.x_dir = 0
                    monster.y_dir = 5
                if z == 2:
                    monster.x_dir = 5
                    monster.y_dir = 0
                if z == 3:
                    monster.x_dir = -5
                    monster.y_dir = 0
                if z == 4:
                    monster.x_dir = 5
                    monster.y_dir = 5
                if z == 5:
                    monster.x_dir = -5
                    monster.y_dir = 5
                if z == 6:
                    monster.x_dir = 5
                    monster.y_dir = -5
                if z == 7:
                    monster.x_dir = -5
                    monster.y_dir = -5

            monster.x += monster.x_dir
            monster.y += monster.y_dir

            if monster.x > width:
                monster.x = 0
            if monster.x < 0:
                monster.x = 510
            if monster.y > height:
                monster.y = 0
            if monster.y < 0:
                monster.y = 480

            # Game logic
            if math.sqrt(math.pow((monster.x - hero.x), 2)
            + math.pow((monster.y - hero.y), 2)) < 32:
                sound.play()
                monster.alive = False

        # Draw background
        screen.fill(blue_color)
        background_image = \
        pygame.image.load('images/background.png').convert_alpha()
        screen.blit(background_image, (0, 0))

        # Game display
        screen.blit(hero.hero_image, (hero.x, hero.y))
        if monster.alive == True:
            screen.blit(monster.monster_image, (monster.x, monster.y))
        if monster.alive == False:
            screen.blit(text, (29, 50))

        pygame.display.update()
        #time.time(2)
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
