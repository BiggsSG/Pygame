import pygame
import random
import math
import time
import sys
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
RED = (255,0,0)
PURPLE = (128,0,128)


## -- Define the class Button which is a sprite 
class Button(pygame.sprite.Sprite): 
    def __init__(self, color, width, height): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 1000
        self.rect.y = 1000
    
    def button_setx_val(self, x):
        self.rect.x = x
    
    def button_sety_val(self, y):
        self.rect.y = y

## -- Define the class NPC which is a sprite 
class NPC(pygame.sprite.Sprite): 
    def __init__(self, color, width, height): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 340
        self.rect.y = 70

## -- Define the class Enemy which is a sprite 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self, color, width, height, HP): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 640
        self.rect.y = 240
        self.HP = 50

    def enemy_setx_val(self, x):
        self.rect.x = x
    
    def enemy_sety_val(self, y):
        self.rect.y = y

    def enemy_attacked(self, damage):
        self.HP = self.HP - damage
    
    def set_enemy_hp(self, health):
        self.HP = health

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite): 
    def __init__(self, color, width, height, HP, MP): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 340
        self.rect.y = 500
        self.movex = 0
        self.movey = 0
        self.HP = 44
        self.MaxHP = 50
        self.MP = 5
        self.MaxMP = 5
        self.Defend = False

    def player_set_movement(self, x, y):
        self.movex += x
        self.movey += y

    def player_end_movement(self):
        self.movex = 0
        self.movey = 0

    def player_x_val(self):
        return self.rect.x
    
    def player_setx_val(self, x):
        self.rect.x = x
    
    def player_sety_val(self, y):
        self.rect.y = y
    
    def set_player_hp(self, health, Max):
        self.HP = health
        self.MaxHP = Max
    
    def set_player_mp(self, magic, Max):
        self.MP = magic
        self.MaxMP = Max
    
    def use_mp(self, magic):
        self.MP = self.MP - magic
    
    def player_heal(self, heal):
        self.HP = self.HP + heal

    def set_defending(self):
        self.Defend = isdefending
        self.HP = self.HP + 5


    def update(self): 
        self.rect.x += self.movex
        self.rect.y += self.movey

        if self.rect.x > 690:
            self.rect.x = 690
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 510:
            self.rect.y = 510
        if self.rect.y < 0:
            self.rect.y = 0

        # Check collision with NPC sprite
        if self.rect.colliderect(NPCr.rect):
            # Adjust player position to prevent overlap
            if self.movex > 0:
                self.rect.right = NPCr.rect.left
            elif self.movex < 0:
                self.rect.left = NPCr.rect.right
            if self.movey > 0:
                self.rect.bottom = NPCr.rect.top
            elif self.movey < 0:
                self.rect.top = NPCr.rect.bottom
        
        # Check collision with Enemy sprite
        if self.rect.colliderect(Enemeyr.rect):
            # Adjust player position to prevent overlap
            if self.movex > 0:
                self.rect.right = Enemeyr.rect.left
            elif self.movex < 0:
                self.rect.left = Enemeyr.rect.right
            if self.movey > 0:
                self.rect.bottom = Enemeyr.rect.top
            elif self.movey < 0:
                self.rect.top = Enemeyr.rect.bottom


# -- Initialise PyGame
pygame.init()
pygame.font.init()
my_fontbig = pygame.font.SysFont('Comic Sans MS', 25)
my_font = pygame.font.SysFont('Comic Sans MS', 18)

# Create a clock object to track time
clock = pygame.time.Clock()

# -- Blank Screen
size = (720, 540)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Turn Based")
# -- Exit game flag set to false
done = False 
# Create a list of all sprites#
enemy_group = pygame.sprite.Group()  # Create a separate group for enemies 
npc_group = pygame.sprite.Group()  # Create a separate group for NPCs
fight_group = pygame.sprite.Group() # Create a separate group for the fighting sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 

# Create the enemies 
Enemeyr = Enemy(RED, 30, 30, 300000)
all_sprites_group.add(Enemeyr) 
enemy_group.add(Enemeyr)
fight_group.add(Enemeyr)

# Create the NPC 
NPCr = NPC(YELLOW, 30, 30)
all_sprites_group.add(NPCr) 
npc_group.add(NPCr)

# Create the player
Player = Player(BLUE, 30, 30, 50, 5)
all_sprites_group.add(Player)
fight_group.add(Player) 

# Buttons
BackdropButton = Button(BLUE, 720, 200)
fight_group.add(BackdropButton)

BackdropButton2 = Button(BLACK, 720, 400)
fight_group.add(BackdropButton2)

Buttonf = Button(WHITE, 120, 32)
fight_group.add(Buttonf)

Buttonh = Button(WHITE, 120, 32)
fight_group.add(Buttonh)

Buttond = Button(WHITE, 120, 32)
fight_group.add(Buttond)

Buttonr = Button(WHITE, 120, 32)
fight_group.add(Buttonr)


click_detector = False
click_detector2 = False

click_detectorf = False
click_detectorh = False
click_detectord = False
click_detectorr = False
isdefending = False

# Initialize variables for cooldowns and last click times
cooldown_f = 0
cooldown_h = 0
cooldown_d = 0
cooldown_r = 0
last_click_time_f = 0
last_click_time_h = 0
last_click_time_d = 0
last_click_time_r = 0
textcooldown_f = 0
textcooldown_h = 0
textcooldown_d = 0
textcooldown_r = 0


# Define cooldown duration (5 seconds)
cooldown_duration = 5


def get_damage():
    return random.randint(1,10)


# sets gamestate to open world, open world = 1 fight = 2
gamestate = 1

### -- Game Loop
while not done:
    if gamestate == 1:
        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and NPCr.rect.collidepoint(event.pos):
                    click_detector = True
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and Enemeyr.rect.collidepoint(event.pos):
                    click_detector2 = True
            elif event.type == pygame.KEYDOWN:  # - a key is down
                if event.key == pygame.K_a:  # - if the left key is pressed
                    Player.player_set_movement(-4, 0)  # speed set to -3
                elif event.key == pygame.K_d:  # - if the right key is pressed
                    Player.player_set_movement(4, 0)  # speed set to 3
                elif event.key == pygame.K_w:
                    Player.player_set_movement(0, -4)
                elif event.key == pygame.K_s:
                    Player.player_set_movement(0, 4)
            elif event.type == pygame.KEYUP:  # - a key released
                if event.key in (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s):
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
                        Player.player_end_movement()  # speed set to 0

        all_sprites_group.update()

        # Clear the screen if no collision
        screen.fill(GREEN)

        all_sprites_group.draw(screen)
        Area1 = my_fontbig.render('Grasslands', False, (255, 255, 255))
        screen.blit(Area1, (5, 5))

        Hint1 = my_font.render('Hint: Click on the yellow sprite', False, (255, 255, 255))
        screen.blit(Hint1, (5, 510))

        # Display "Success" if NPC sprite is clicked
        if click_detector:
            n_txt = my_font.render('Welcome, walk over to the enemy', False, (255, 255, 255))
            n_txt2 = my_font.render('and click to intiate a fight', False, (255, 255, 255))
            screen.blit(n_txt, (230, 20))
            screen.blit(n_txt2, (260, 40))

        if click_detector2:
            e_txt = my_font.render('Fight initated', False, (255, 255, 255))
            screen.blit(e_txt, (600, 200))
            gamestate = 2
        
    if gamestate == 2:
        #variable used for checking for cooldowns
        current_time = pygame.time.get_ticks()  # Get current time in milliseconds
        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(GREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            #variable used for checking for cooldowns
            current_time = time.time()
            # Check if the mouse button was clicked on the NPC sprite
            if event.button == 1 and Buttonf.rect.collidepoint(event.pos):
                if current_time - last_click_time_f >= cooldown_duration:
                    click_detectorf = True
                    last_click_time_f = current_time
               

            if event.button == 1 and Buttonh.rect.collidepoint(event.pos):
                if current_time - last_click_time_h >= cooldown_duration:
                    click_detectorh = True
                    last_click_time_h = current_time
        

            if event.button == 1 and Buttond.rect.collidepoint(event.pos):
                if current_time - last_click_time_d >= cooldown_duration:
                    click_detectord = True
                    last_click_time_d = current_time

            if event.button == 1 and Buttonr.rect.collidepoint(event.pos):
                if current_time - last_click_time_r >= cooldown_duration:
                    click_detectorr = True
                    last_click_time_r = current_time


        if click_detectorf:
            damage = get_damage()
            Enemeyr.enemy_attacked(damage)
            f_txt = my_font.render('You attacked the Test Dummy', False, (255, 255, 255))
            f_txt2 = my_font.render('You dealt ' + str((damage)) + ' damage', False, (255, 255, 255))
            screen.blit(f_txt, (230, 20))
            screen.blit(f_txt2, (260, 40))
            click_detectorf = False
            if Enemeyr.HP <= 0:
             end_txt = my_font.render('You killed the Test Dummy', False, (255, 255, 255))
             screen.blit(end_txt, (230, 60))  
        
        if click_detectorh:
            if Player.HP == Player.MaxHP:
                hf_txt = my_font.render('You can not heal over max HP', False, (255, 255, 255))
                screen.blit(hf_txt, (230, 20))   
            if Player.HP < Player.MaxHP: 
                Player.use_mp(1)
                if Player.HP >= 45:
                    Player.HP = 50
                    h_txt = my_font.render('You have healed to full', False, (255, 255, 255))
                    screen.blit(h_txt, (230, 20))
                if Player.HP < 45:
                    Player.player_heal(5)
                    h2_txt = my_font.render('You have successfully healed', False, (255, 255, 255))
                    screen.blit(h2_txt, (230, 20))   
                if Player.MP <= 0:
                    Player.MP = 0
            click_detectorh = False
        
        if click_detectord:
            isdefending = True
            Player.set_defending
            d_txt = my_font.render('You have successfully defended', False, (255, 255, 255))
            screen.blit(d_txt, (230, 20))
            click_detectord = False

        
        if click_detectorr:
            r_txt = my_font.render('You can not flee from this battle', False, (255, 255, 255))
            screen.blit(r_txt, (230, 20))
            click_detectorr = False    

        #set player pos
        Player.player_setx_val(240)
        Player.player_sety_val(175)

        #set enemy pos
        Enemeyr.enemy_setx_val(450)
        Enemeyr.enemy_sety_val(175)

        #set fight button pos
        Buttonf.button_setx_val(40)
        Buttonf.button_sety_val(365)

        #set heal button pos
        Buttonh.button_setx_val(40)
        Buttonh.button_sety_val(410)
                
        #set defend button pos
        Buttond.button_setx_val(40)
        Buttond.button_sety_val(455)
                
        #set flee button pos
        Buttonr.button_setx_val(40)
        Buttonr.button_sety_val(500)

        #set backdropbutton pos
        BackdropButton.button_setx_val(0)
        BackdropButton.button_sety_val(350)

        #set backdrop2button pos
        BackdropButton2.button_setx_val(200)
        BackdropButton2.button_sety_val(550)

        #draw the fighting sprites and buttons
        fight_group.update()
        fight_group.draw(screen)

        #draw the hp bar
        pygame.draw.rect(screen, BLACK, (335, 374, Player.MaxHP*3 + 3, 24))
        pygame.draw.rect(screen, RED, (335, 374, Player.MaxHP*3, 20))
        pygame.draw.rect(screen, GREEN, (335, 374, Player.HP*3, 20))

        #draw the magic bar
        pygame.draw.rect(screen, BLACK, (335, 409, Player.MaxMP*30 + 3, 24))
        pygame.draw.rect(screen, RED, (335, 409, Player.MaxMP*30, 20))
        pygame.draw.rect(screen, PURPLE, (335, 409, Player.MP*30, 20))

        #set area text
        Area2 = my_fontbig.render('Grasslands: Fight', False, (255, 255, 255))
        screen.blit(Area2, (5, 5))

        #set button texts
        Button1 = my_fontbig.render('Fight', False, (0, 0, 0))
        screen.blit(Button1, (45, 361))
        Button2 = my_fontbig.render('Heal', False, (0, 0, 0))
        screen.blit(Button2, (45, 410))
        Button3 = my_fontbig.render('Defend', False, (0, 0, 0))
        screen.blit(Button3, (45, 455))
        Button4 = my_fontbig.render('Flee', False, (0, 0, 0))
        screen.blit(Button4, (45, 500))
        Health = my_fontbig.render('HP:' + str(Player.HP) + "/" + str(Player.MaxHP), False, (0, 0, 0))
        screen.blit(Health, (200, 365))
        MagicP = my_fontbig.render('MP:' + str(Player.MP) + "/" + str(Player.MaxMP), False, (0, 0, 0))
        screen.blit(MagicP, (200, 400))

        #draw button backdrops
        #fight backdrop
        pygame.draw.rect(screen, BLACK, (160, 365, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 397, 123, 6))

        #heal backdrop
        pygame.draw.rect(screen, BLACK, (160, 410, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 442, 123, 6))

        #defend backdrop
        pygame.draw.rect(screen, BLACK, (160, 455, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 487, 123, 6))

        #flee backdrop
        pygame.draw.rect(screen, BLACK, (160, 500, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 532, 123, 6))

        #draw bar encasing
        pygame.draw.rect(screen, BLACK, (180, 365, 4, 170))
        pygame.draw.rect(screen, BLACK, (526, 365, 4, 170))
        pygame.draw.rect(screen, BLACK, (180, 532, 350, 4))
        pygame.draw.rect(screen, BLACK, (180, 365, 350, 4))

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

# End While
pygame.quit()