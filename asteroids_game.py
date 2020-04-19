import pygame
from random import randint
import time
pygame.init()
window_height = 500
window_width = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("asteroids")
player_lost = False
run = True
bullets = []
enemies = []
score = 0
gameDisplay = pygame.display.set_mode((window_width,window_height))
max_enemies = 1
def pregame():
    window.fill((0,0,0))
    message_display("Shoot the enemies with the spacebar",0,0,3,25)
    message_display("You can only have 4 bullets at a time",0,0,3,25)
    message_display("Move with the sideways arrow keys",0,0,3,25)
    message_display("Don't let any enemies reach the bottom of the screen!",0,0,3,18)
    message_display("READY!",0,0,.7,40)
    message_display("SET!",0,0,.7,40)
    message_display("GO!",0,0,.7,40)

def text_objects(text, font):
    textSurface = font.render(text, True, (100,100,100))
    return textSurface, textSurface.get_rect()
def end_game():
    bullets.clear()
    enemies.clear()
    run = False
    player_lost == True
    message_display("Game Over!",0,0,1.5, 80)
    message_display("Round - " + str(max_enemies),0,0,1.5,80)
    message_display("Score - " + str(score),0,0,1.5, 70)
    run = False
    pygame.quit()
def message_display(text, offcenter_x, offcenter_y, delay, size):
    bullets = []
    enemies = []
    window.fill((0,0,0))
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window_width//2) + offcenter_x,(window_height//2) + offcenter_y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(delay)

def restart_game():
    print ("yeet")
    message_display("Would you like to restart?", 0, -50,3, 40)

    repeater = True
    while repeater:
        print(str(len(enemies)))
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            enemies.append(Enemy(100,0,(200,100,0),20,20,3,1 ,1))
            repeater = False
            break
        if keys[pygame.K_n]:
            repeater = False
            run = False
            break
class Character(object):
    def __init__(self,x,y, width,vertex1, vertex2, vertex3,height, vel,wideness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wideness = wideness
        self.vertex1 = (self.x, self.y - self.height)
        self.vertex2 = (int(self.x + (self.wideness/2)), self.y)
        self.vertex3 = (int(self.x - (self.wideness/2)), self.y)
        self.vel = vel
    def change_vertex(self, direction, amnt_change):
        if direction == "U":
            self.y -= amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "D":
            self.y += amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "L":
            self.x -= amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "R":
            self.x += amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (self.x + (self.wideness // 2), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        else:
            pass
    def move_char(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if (self.x + (self.wideness/2)) + 1 < (window_width):
                self.x += self.vel
                self.change_vertex("R", self.vel)

        if keys[pygame.K_LEFT]:
            if self.x - (self.wideness/2) > 1:
                self.x -= self.vel
                self.change_vertex("L", self.vel)

        # if keys[pygame.K_UP]:
        #     if self.y > self.height:
        #         self.y -= self.vel
        #         self.change_vertex("U", self.vel)
        #
        # if keys[pygame.K_DOWN]:
        #     if self.y < (window_height):
        #         self.y += self.vel
        #         self.change_vertex("D", self.vel)
bob = Character(200,(window_height-35),1,(20,30),(22,20),(18,20),20, 1, 6)
enemys_number = 1
class Bullet(object):
    def __init__(self, x, y, radius, color, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = width
    def show(self):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius)
    def move(self):
        if self.y <= 0:
            bullets.pop(bullets.index(self))
        else:
            self.y -= 3
    def return_x_hitbox(self):
        i = []
        i.append(self.x - self.radius)
        i.append(self.x + self.radius)
        return self.x - self. radius, self.x + self.radius
    def return_y_hitbox(self):
        i = []
        i.append(self.y - self.radius)
        i.append(self.y + self.radius)
        return self.y - self.radius, self.y +self.radius
class Enemy(object):
    def __init__(self, x, y, color, height, wideness, speed, direction, down_var):
        self.x = x
        self.y = y
        self.height = randint(20,35)
        self.wideness = randint(15,40)
        self.color = color
        self.speed = speed
        self.direction = direction
        self.down_var = down_var
    def show(self):
        pygame.draw.polygon(window,self.color, [(self.x, self.y + self.height),(self.x + (self.wideness//2), self.y),(self.x - (self.wideness//2), self.y)])
    def move(self):
        if self.y >= window_height:
            end_game()
        elif self.direction == 1:
            if self.x + (self.wideness//2) <= window_width:
                self.x += self.speed
                if self.down_var == 1:
                    self.y += self.speed//2
                    self.down_var -=1
                else:
                    self.down_var = 1
            else:
                self.x -= self.speed
                self.direction = -1
                if self.down_var == 1:
                    self.y += self.speed//2
                    self.down_var -=1
                else:
                    self.down_var = 1
        elif self.direction == -1:
            if self.x - (self.wideness//2) >= 0:
                self.x -= self.speed
                if self.down_var == 1:
                    self.y += self.speed//2
                    self.down_var -=1
                else:
                    self.down_var = 1
            else:
                self.x += self.speed
                self.direction = 1
                if self.down_var == 1:
                    self.y += self.speed//2
                    self.down_var -=1
                else:
                    self.down_var = 1
    def return_x_hitbox(self):
        i = []
        i.append(self.x - (self.wideness//2))
        i.append(self.x + (self.wideness//2))
        return i
    def return_y_hitbox(self):
        i = []
        i.append(self.y)
        i.append(self.y +self.height)
        return i
    def check_hit(self, bullet_x, bullet_y):
        if self.return_x_hitbox() :
            pass
gurt = Enemy(100,0,(200,100,0),20,20,3,1 ,1)
enemies.append(gurt)
being_held = False
pregame()
while run:
    pygame.time.delay(15)
    if player_lost:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    bob.move_char()
    keys = pygame.key.get_pressed()
    if being_held ==  False:
        if keys[pygame.K_SPACE]:
            being_held = True
            if len(bullets) <= 3:
                bullets.append(Bullet(bob.x, (bob.y - bob.height), 5, (50,200,50 ), 1))
    else:
        if keys[pygame.K_SPACE]:
            being_held = True
        else:
            being_held = False
    window.fill((0,0,0))
    for e in enemies:
        e.show()
        e.move()
        if e.y >= window_height:
            end_game()
    for bullet in bullets:
        bullet.show()
        bullet.move()
        for enemy in enemies:

            ei = enemies.index(enemy)
            if enemy.return_x_hitbox()[1] >= bullet.return_x_hitbox()[0]:
                if enemy.return_x_hitbox()[0] <= bullet.return_x_hitbox()[1]:
                    if enemy.return_y_hitbox()[1] >= bullet.return_y_hitbox()[0]:
                        if enemy.return_y_hitbox()[0] <= bullet.return_y_hitbox()[1]:
                            enemies.pop(ei)
                            if bullet in bullets:
                                bullets.pop(bullets.index(bullet))
                            enemys_number -= 1
                            score += 1
                            if enemys_number <= 0:
                                max_enemies += 1
                                for i in range(max_enemies):
                                    enemies.append(Enemy((randint(0,window_width)),0,(200,100,0),randint(10,25), randint(20,40), 3, 1,1))
                                    enemys_number += 1
    pygame.draw.polygon(window, (200,200,200), [bob.vertex1, bob.vertex2, bob.vertex3], bob.width)
    pygame.display.update()
pygame.quit()