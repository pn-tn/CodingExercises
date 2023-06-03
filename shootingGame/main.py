import threading as th
import numpy as np
import time
import pygame
import random
import math

'''
CSCC 31 - Multithreading Project
Multithreaded Shooting Game

Sendad, Aloysius Hasheem A.

'''


# == Globals ==

# size of screen
x = 1080
y = 900

score = 0
player_pos = [x/2, y/2]
hit = [0, 0]
speed = 0
thread_running = True
recoil = False
running = True


# == /Globals ==

# thread this
class Enemy:
    global x,y
    global thread_running
    global hit
    def __init__(self, screen, number):
        self.x = 123
        self.y = 123
        self.screen = screen
        self.hitbox = [self.x, self.y, self.x+60, self.y+60]

    def spawn(self, screen):
        self.rawr = pygame.image.load('images/rawr.png')
        self.screen.blit(self.rawr, (self.x, self.y))

    def die(self):  # i'm die thank you forever
        global speed
        global score

        # if enemy is hit
        if hit[0] > self.x and hit[0] < self.x + 60 and hit[1] > self.y and hit[1] < self.y + 60:
            score += 69
            speed += 1
            print("hit. score: ", score)
        # if hit at exact center
        if hit[0] == self.x and hit[1] == self.y:
            score += 420
            speed += 1
            print("hit. score: ", score)

    def run(self):
        global speed
        print("Thread for enemy starting...")
        hitBottom = False
        hitRight = False
        while thread_running:
            # sleep because enemy will be too fast
            time.sleep(0.01)

            # collision on edges
            if self.y >= y-60:
                hitBottom = True
            elif self.y < 0:
                hitBottom = False

            if self.x >= x-60:
                hitRight = True
            elif self.x < 0:
                hitRight = False

            if hitBottom == True:
                self.y -= speed
            elif hitBottom == False:
                self.y += speed

            if hitRight == True:
                self.x -= speed
            elif hitRight == False:
                self.x += speed

            self.hitbox = [self.x, self.y, self.x+60, self.y+60]
        print("Enemy thread exited")


class Player:
    global hit
    global thread_running
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.hitbox = [self.x, self.y, self.x + 60, self.y + 80]


    def draw_char(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # code for the gun to face cursor
        start_angle = [1, 0]                    # along the x-axis
        vec_1 = [self.x + 30, self.y + 40]      # position of player
        vec_2 = [mouse_x, mouse_y]              # position of cursor

        i = vec_2[0] - vec_1[0]
        j = vec_2[1] - vec_1[1]

        target_pos = [i, j]

        # this only gets the smaller angle of the 360 circle
        unit_start_angle = start_angle / np.linalg.norm(start_angle)
        unit_target_pos = target_pos / np.linalg.norm(target_pos)
        dot_product = np.dot(unit_start_angle, unit_target_pos)
        angle = np.arccos(dot_product)
        # thus, negative if clicked from opposite angle
        if mouse_y < self.y:
            angle = (0 - angle)

        deg_angle = -math.degrees(angle)

        if mouse_x < self.x:
            self.gun = pygame.image.load('images/gun_l.png')
            self.person = pygame.image.load('images/person_l.png')
            rotateGun = pygame.transform.rotate(self.gun, deg_angle - 180)
            self.screen.blit(self.person, (self.x, self.y))
            self.screen.blit(rotateGun, (self.x - 20, self.y))
        else:
            self.gun = pygame.image.load('images/gun_r.png')
            self.person = pygame.image.load('images/person_r.png')
            rotateGun = pygame.transform.rotate(self.gun, deg_angle)
            self.screen.blit(self.person, (self.x, self.y))
            self.screen.blit(rotateGun, (self.x, self.y))

        self.hitbox = [self.x, self.y, self.x + 60, self.y + 80]


    def shoot(self, x, y):
        global recoil
        hit[0] = x
        hit[1] = y
        recoil = True
        print(hit)

    # thread this
    def run(self):
        global recoil
        global hit
        global x, y
        print("Thread for player starting...")
        cursor = None
        while thread_running:
            if recoil:
                cursor = hit
                print("aa: ", cursor)

                # calculation for angle
                start_angle = [1, 0]                    # along the x-axis

                # size of player is 60x80
                vec_1 = [self.x + 30, self.y + 40]      # position of player
                vec_2 = [cursor[0], cursor[1]]          # position of cursor

                i = vec_2[0] - vec_1[0]
                j = vec_2[1] - vec_1[1]

                target_pos = [i, j]

                # this only gets the smaller angle of the 360 circle
                unit_start_angle = start_angle / np.linalg.norm(start_angle)
                unit_target_pos = target_pos / np.linalg.norm(target_pos)
                dot_product = np.dot(unit_start_angle, unit_target_pos)
                angle = np.arccos(dot_product)
                # thus, negative if clicked from opposite angle
                if cursor[1] < self.y:
                    angle = (0 - angle)

                # this is just for display
                print(angle, " -> ", math.degrees(angle))

                bounceLR = False
                bounceUD = False
                for i in range(15):
                    time.sleep(0.01)



                    # implementing bounce on walls
                    if x < self.x+60:
                        bounceLR = True
                    elif self.x < 0:
                        bounceLR = True
                    if y < self.y+80:
                        bounceUD = True
                    elif self.y < 0:
                        bounceUD = True

                    if bounceLR:
                        self.x += (15-i) * (math.cos(angle))
                    else:
                        self.x += (15-i) * -(math.cos(angle))

                    if bounceUD:
                        self.y += (15-i) * (math.sin(angle))
                    else:
                        self.y += (15-i) * -(math.sin(angle))

                bounceLR = False
                bounceUD = False

                recoil = False
        print("Player thread exited")


# my original plan is to thread this as well
# but threading this makes my pc laggy idk why
# so I decided not to
def checkCollision(player, enemy):
    global running

    # self.hitbox is an array of [x, y, x+top, y+top]
    if enemy.hitbox[0] > player.hitbox[0] and enemy.hitbox[0] < player.hitbox[2]:
        if enemy.hitbox[1] > player.hitbox[1] and enemy.hitbox[1] < player.hitbox[3]:
            running = False
    if enemy.hitbox[2] > player.hitbox[0] and enemy.hitbox[2] < player.hitbox[2]:
        if enemy.hitbox[3] > player.hitbox[1] and enemy.hitbox[3] < player.hitbox[3]:
            running = False

    if player.hitbox[0] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[2]:
        if player.hitbox[1] > enemy.hitbox[1] and player.hitbox[1] < enemy.hitbox[3]:
            running = False
    if player.hitbox[2] > enemy.hitbox[0] and player.hitbox[2] < enemy.hitbox[2]:
        if player.hitbox[3] > enemy.hitbox[1] and player.hitbox[3] < enemy.hitbox[3]:
            running = False


# my main method owo
def main():
    global x, y
    global thread_running
    global score
    global running

    screen = pygame.display.set_mode([x,y])
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)

    cursor_img = pygame.image.load('images/crosshair.png')
    cursor_rect = cursor_img.get_rect()
    pygame.mouse.set_visible(False)
    # create character
    me = Player(player_pos[0],player_pos[1], screen)
    enemy = Enemy(screen, 10)

    # create threads
    en = th.Thread(target = enemy.run, args=())
    en.start()
    meee = th.Thread(target = me.run, args=())
    meee.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                posx, posy = pygame.mouse.get_pos()
                me.shoot(posx, posy)

        screen.fill((40,44,52))

        # display score
        s = "Score: " + str(score)
        text_surface = my_font.render(s , False, (255, 255, 255))
        screen.blit(text_surface, (0,0))



        enemy.spawn(screen)
        enemy.die()

        me.draw_char()

        checkCollision(me, enemy)

        # reset hit
        hit[0] = 0
        hit[1] = 0

        cursor_rect.center = pygame.mouse.get_pos()     # update position
        screen.blit(cursor_img, cursor_rect)            # draw the cursor

        pygame.display.flip()

    thread_running = False
    pygame.quit()

    # game over screen
    go_screen = pygame.display.set_mode([x/2,y/2])
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
    gameOver = True
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
        go_screen.fill((40,44,52))

        # GAME OVER
        go = "GAME OVER!!"
        GO_surface = my_font2.render(go , False, (255, 255, 255))
        go_screen.blit(GO_surface, (130,100))
        # display score
        s = "Your Score: " + str(score)
        text_surface = my_font.render(s , False, (255, 255, 255))
        go_screen.blit(text_surface, (200,260))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
